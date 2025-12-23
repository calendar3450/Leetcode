class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix2 = matrix.copy()
        
        for c in range(n):
            tmp = []
            for r in range(n-1,-1,-1):
                tmp.append(matrix2[r][c])
            matrix[c] = tmp
