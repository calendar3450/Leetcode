from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        queue = deque()
        fresh = 0

        for i in range(row):
            for j in range(col):

                if grid[i][j] == 2:
                    queue.append((i,j))

                elif grid[i][j] == 1:
                    fresh+=1
        time = 0

        while queue and fresh >0:
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for dx,dy in dir:
                    nx = x + dx
                    ny = y + dy
                    if 0<=nx<row and 0<=ny<col and grid[nx][ny] ==1:
                        grid[nx][ny] = 2
                        fresh-=1
                        queue.append((nx,ny))
            time +=1

        return time if fresh == 0 else -1