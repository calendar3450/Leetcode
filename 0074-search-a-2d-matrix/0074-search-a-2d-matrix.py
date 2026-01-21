class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        tmp = []

        for i in matrix:
            tmp +=i

        if target not in tmp:
            return False

        else:
            return True