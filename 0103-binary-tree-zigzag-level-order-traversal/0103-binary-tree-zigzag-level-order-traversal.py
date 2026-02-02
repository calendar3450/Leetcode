from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        q = deque([root])
        level = 0

        while q:
            size = len(q)
            cur = deque()

            for i in range(size):
                node = q.popleft()

                if level %2 ==0:
                    cur.append(node.val)
                else:
                    cur.appendleft(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(list(cur))
            level +=1

        return result
            
            