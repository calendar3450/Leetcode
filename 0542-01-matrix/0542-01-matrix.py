from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        cnt = 0
        move = [(-1,0),(1,0),(0,1),(0,-1)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = -1

        while queue:
            i,j = queue.popleft()
            
            for di,dj in move:
                ni,nj = i+di,j+dj

                if 0 <= ni < m and 0 <= nj < n and mat[ni][nj] == -1:
                    mat[ni][nj] = mat[i][j] + 1
                    queue.append((ni, nj))

        return mat
            

                

                

                

