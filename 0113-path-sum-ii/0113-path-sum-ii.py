# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer=[]
        if not root:
            return []

        def backtracking(cur,node):
            print(cur)
            if not node:
                return
            if not node.right and not node.left and sum(cur) == targetSum:
                answer.append(cur.copy())
                return

            if node.left:
                cur.append(node.left.val)
                backtracking(cur,node.left)
                cur.pop()
            if node.right:
                cur.append(node.right.val)
                backtracking(cur,node.right)
                cur.pop()
        
        backtracking([root.val],root)

        return answer

