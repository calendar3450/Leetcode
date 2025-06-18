# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def DFS(node):
            if not node:
                return 0

            leftDFS = DFS(node.left)
            rightDFS = DFS(node.right)

            self.diameter = max(self.diameter,leftDFS + rightDFS)

            return max(leftDFS,rightDFS)+1

        DFS(root)
        return self.diameter