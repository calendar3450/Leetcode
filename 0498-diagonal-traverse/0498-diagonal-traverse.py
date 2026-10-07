class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        ans = []
        row = len(mat)
        col = len(mat[0])
        check = row+col -1

        for i in range(check):
            if i %2 ==0:
                start_r = min(i,row-1)
                start_c = i-start_r

                while 0<=start_r<row and 0<=start_c<col:
                    ans.append(mat[start_r][start_c])
                    start_r-=1
                    start_c+=1

            else:
                start_c = min(i,col-1)
                start_r = i-start_c

                while 0<=start_r<row and 0<=start_c<col:
                    ans.append(mat[start_r][start_c])
                    start_r+=1
                    start_c-=1

        return ans