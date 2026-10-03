class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        result_len = (bottom+1) * (right+1)
        
        while len(result) < result_len:
            # 왼쪽에서 오른쪽 이동
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top +=1

            if len(result) == result_len:
                break

            # 위에서 아래로 이동
            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right-=1

            if len(result) == result_len:
                break

            # 오른쪽에서 왼쪽으로 이동
            for i in range(right,left-1,-1):
                result.append(matrix[bottom][i])
            bottom -=1

            if len(result) == result_len:
                break

            # 아래에서 위로 이동
            for i in range(bottom,top-1,-1):
                result.append(matrix[i][left])
            left+=1

        return result
            

            