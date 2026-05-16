# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        numbers = []

        def DFS(node):
            if not node:
                return

            numbers.append(node.val)
            DFS(node.right)
            DFS(node.left)

        DFS(root)

        numbers.sort()
 
        for idx,num in enumerate(numbers):
            if idx+1 == k:
                return num