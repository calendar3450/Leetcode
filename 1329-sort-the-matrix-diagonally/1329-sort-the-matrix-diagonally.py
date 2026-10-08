from collections import defaultdict
class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        diagnoal_dict = defaultdict(list)
        row = len(mat)
        col = len(mat[0])

        for i in range(row):
            for j in range(col):
                diagnoal_dict[i-j].append(mat[i][j])

        for value in diagnoal_dict.values():
            value.sort(reverse = True)

        for r in range(row):
            for c in range(col):
                mat[r][c] = diagnoal_dict[r - c].pop()
        
        return mat