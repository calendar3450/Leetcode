class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtracking(path, open, close):
            if len(path) == 2*n:
                result.append(path)
                return
            
            if open < n:
                backtracking(path+'(',open+1,close)

            if close < open:
                backtracking(path+')',open,close+1)

        backtracking('',0,0)


        return result
