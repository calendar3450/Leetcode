from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        
        # def BFS(x,y):
        #     queue = deque()
        #     queue.append((x,y))
        #     grid[x][y] ="0"
            
        #     while queue:
        #         x,y = queue.popleft()
        #         if grid[x][y] != "0":
        #             if 0<=x+1<m:
        #                 queue.append((x+1,y))
        #             if 0<=x-1<m:
        #                 queue.append((x-1,y))
        #             if 0<=y+1<n:
        #                 queue.append((x,y+1))
        #             if 0<=y-1<n:
        #                 queue.append((x,y-1))

        def BFS(x, y):
            queue = deque()
            queue.append((x, y))
            grid[x][y] = "0"
            
            while queue:
                x, y = queue.popleft()
                
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<n and 0<=ny<m and grid[nx][ny] == "1":  # 범위 + '1' 체크
                        grid[nx][ny] = "0"   # 즉시 방문처리
                        queue.append((nx, ny))

        for y in range(m):
            for x in range(n):
                if grid[x][y] == "1":
                    BFS(x,y)
                    ans +=1

        return ans