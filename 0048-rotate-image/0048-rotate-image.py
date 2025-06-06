class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        tmp = [row[:] for row in matrix]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = tmp[n-1-j][i]
        