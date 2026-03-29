class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_end = None

        root = TrieNode()

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end= word

        row = len(board)
        col = len(board[0])
        result = []

        def DFS(x,y,node):
            ch= board[y][x]

            if ch not in node.children:
                return
            
            next_node = node.children[ch]

            if next_node.is_end:
                result.append(next_node.is_end)
                next_node.is_end = None
            
            board[y][x] = '#'  # 방문 처리 (check 배열 대신)

            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < col and 0 <= ny < row and board[ny][nx] != '#':
                    DFS(nx, ny, next_node)

            board[y][x] = ch  # 복구
        
        for i in range(row):
            for j in range(col):
                DFS(j,i,root)

        return result