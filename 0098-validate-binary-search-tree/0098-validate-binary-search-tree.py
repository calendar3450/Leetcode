class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if node is None:
                return True

            # 현재 노드의 값이 허용 범위를 벗어나면 False 반환
            if not (low < int(node.val) < high):
                return False

            # 왼쪽 서브트리는 high 값을 현재 노드로 설정하여 재귀 호출
            # 오른쪽 서브트리는 low 값을 현재 노드로 설정하여 재귀 호출
            return dfs(node.left, low, int(node.val)) and dfs(node.right, int(node.val), high)

        # 초기 범위는 (-무한대, +무한대)
        return dfs(root, float('-inf'), float('inf'))
