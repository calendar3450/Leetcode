from collections import deque

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        # 1) 시작점 찾기 (*)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    sx, sy = i, j
                    break
        
        # 2) 반복형 BFS: (x, y, dist)
        q = deque([(sx, sy, 0)])
        # 시작점만 방문 표시
        grid[sx][sy] = 'X'
        
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            x, y, dist = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                # 범위 벗어나거나 벽이면 스킵
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if grid[nx][ny] == 'X':
                    continue
                # 음식 찾으면 즉시 반환
                if grid[nx][ny] == '#':
                    return dist + 1
                # 빈 칸 방문 표시 후 enqueue
                grid[nx][ny] = 'X'
                q.append((nx, ny, dist + 1))
        
        return -1
