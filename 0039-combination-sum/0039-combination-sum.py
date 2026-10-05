class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        answer = []
        n = len(candidates)

        def backtracking(cand,start):
            
            if sum(cand) == target:
                answer.append(cand.copy())
                return
            elif sum(cand) > target:
                return
            
            for i in range(start,n):
                cand.append(candidates[i])
                backtracking(cand,i)
                cand.pop()
            
        
        backtracking([],0)
        
        return answer