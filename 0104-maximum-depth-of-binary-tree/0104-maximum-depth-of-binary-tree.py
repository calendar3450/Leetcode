# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def DFS(node, curLevel):
            nonlocal answer
            if not node:
                answer = max(curLevel-1,answer)
                return
            
            DFS(node.left,curLevel +1)
            DFS(node.right,curLevel +1)

        DFS(root, 1)
        
        return answer