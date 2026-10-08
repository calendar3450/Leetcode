from collections import defaultdict

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diag_dict = defaultdict(list)
        check = n*2-1

        for i in range(check):
            start_r = max(n-1-i,0)
            start_c = max(i - n + 1, 0) 

            while 0<= start_r < n and 0<= start_c <n:
                diag_dict[i].append(grid[start_r][start_c])
                start_r +=1
                start_c +=1
        
        for i in range(check):
            if i >=n:
                diag_dict[i].sort(reverse=True)
            else:
                diag_dict[i].sort()

        for i in range(check):
            start_r = max(n-1-i,0)
            start_c = max(i - n + 1, 0)

            while 0<= start_r < n and 0<= start_c <n:
                grid[start_r][start_c] = diag_dict[i].pop()
                start_r +=1
                start_c +=1

        return grid

        