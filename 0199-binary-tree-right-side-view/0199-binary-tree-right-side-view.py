# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        result = []

        def DFS(node, level):
            if not node:
                return
            
            if len(result) == level:
                result.append(node.val)
            DFS(node.right,level+1)
            DFS(node.left,level+1)

        DFS(root,0)
        return result

