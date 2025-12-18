class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val =='.':
                    empties.append((i,j))
                else:
                    b = (i//3) *3 +(j//3)
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[b].add(val)
        
        def dfs(idx):
            if idx == len(empties):
                return True

            i, j = empties[idx]
            b = (i//3) *3 +(j//3)

            for d in "123456789":
                if d in rows[i] or d in cols[j] or d in boxes[b]:
                    continue

                board[i][j] = d
                rows[i].add(d)
                cols[j].add(d)
                boxes[b].add(d)

                if dfs(idx+1):
                    return True

                board[i][j] = '.'
                rows[i].remove(d)
                cols[j].remove(d)
                boxes[b].remove(d)

            return False

        dfs(0)
