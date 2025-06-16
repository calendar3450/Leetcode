import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        time = 0
        fresh = 0
        rotten_dir = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_dir.append([i,j])

                elif grid[i][j] == 1:
                    fresh +=1

        direction =[(1,0),(0,1),(-1,0),(0,-1)]

        while rotten_dir and fresh >0:
            for _ in range(len(rotten_dir)):
                i,j=rotten_dir.popleft()
                for di,dj in direction:
                    ni , nj = di+i,dj+j
                    if 0<=ni< m and 0<=nj < n and grid[ni][nj] ==1:
                        grid[ni][nj] =2
                        fresh -=1
                        rotten_dir.append((ni,nj))
            time +=1

        return time if fresh == 0 else -1
        

            