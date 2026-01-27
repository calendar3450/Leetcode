class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        columns = len(board[0])
        rows = len(board)
        ans = False
        visited = [[False] * columns for _ in range(rows)]
        moves = [[0,1],[0,-1],[1,0],[-1,0]]

        def BFS(cur_word,x,y):
            nonlocal ans

            if cur_word == word and not ans:
                ans = True
                return
            elif len(cur_word) == len(word):
                return

            for move in moves:
                dx,dy = move[0],move[1]
                nx = x+dx
                ny = y+dy

                if 0<=nx<rows and 0<=ny<columns and not visited[nx][ny]:
                    if board[nx][ny] == word[len(cur_word)]:
                        visited[nx][ny] = True
                        BFS(cur_word + board[nx][ny],nx,ny)
                        visited[nx][ny] = False

        for i in range(rows):
            for j in range(columns):
                if word[0] == board[i][j]:
                    visited[i][j] = True
                    BFS(board[i][j],i,j)
                    visited[i][j] = False

        return ans
