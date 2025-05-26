# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def DFS(root):
            if not root or root is p or root is q:
                return root

            left = DFS(root.left)
            right = DFS(root.right)

            if left and right:
                return root
            return left if left else right

        return DFS(root)
