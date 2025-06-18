# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        
        def DFS(node, i):
            if not node:
                return
            if len(result) == i:
                result.append(node.val)
            DFS(node.right, i+1)
            DFS(node.left,i+1)

        DFS(root,0)
        return result
            