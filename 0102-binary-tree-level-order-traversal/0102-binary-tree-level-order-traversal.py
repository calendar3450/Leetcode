from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []

        def DFS(node, level):
            if not node:
                return

            if len(answer) < level+1:
                answer.append([node.val])
            else:
                answer[level].append(node.val)

            DFS(node.left,level+1)
            DFS(node.right,level+1)
        
        DFS(root,0)

        return answer

            


        