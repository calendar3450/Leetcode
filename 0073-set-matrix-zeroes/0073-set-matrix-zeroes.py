class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix[0])
        column = len(matrix)
        is0 = [[False for _ in range(row)] for _ in range(column)]

        for i in range(column):
            for j in range(row):
                if matrix[i][j] ==0:
                    is0[i][j] = True
        print(is0)
        for i in range(column):
            for j in range(row):
                if is0[i][j]:
                    for k in range(column):
                        matrix[k][j] = 0
                    for l in range(row):
                        matrix[i][l] = 0
