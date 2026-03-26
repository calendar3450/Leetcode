class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            l = 0
            r = col-1
            while l<=r:
                mid = (l+r)//2
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid] > target:
                    r-=1
                else:
                    l+=1

        return False

