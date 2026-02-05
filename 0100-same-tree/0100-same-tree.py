# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pList = []
        qList = []

        def treeToList(node):
            if not node:
                pList.append('null')
                return
            
            pList.append(node.val)
            treeToList(node.left)
            treeToList(node.right)

        treeToList(q)
        qList = pList.copy()
        pList = []
        treeToList(p)

        if pList == qList:
            return True
        else:
            return False
