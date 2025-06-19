class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        mappings ={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        result = []
        def backtracking(index,char):
            if len(digits) == index:
                result.append(char)
                return

            for i in mappings[digits[index]]:
                backtracking(index+1,char+i)
        
        backtracking(0,'')

        return result