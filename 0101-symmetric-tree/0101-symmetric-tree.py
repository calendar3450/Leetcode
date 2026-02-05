# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        rightSide=  root.right
        leftSide = root.left
        checking = []
        
        def DFS(leftNode, rightNode):
            if not leftNode and not rightNode:
                return
            elif not leftNode and rightNode:
                checking.append(False)
                return
            elif leftNode and not rightNode:
                checking.append(False)
                return
        
            if leftNode.val == rightNode.val:
                DFS(leftNode.right, rightNode.left)
                DFS(leftNode.left, rightNode.right)
            else:
                checking.append(False)

        DFS(leftSide,rightSide)

        if checking:
            return False
        else:
            return True