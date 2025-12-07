class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        strs = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        def backtracking(index, path):
            if index == len(digits):
                result.append(path)
                return

            for char in strs[digits[index]]:
                backtracking(index +1, path + char)
        
        backtracking(0,'')


        return result