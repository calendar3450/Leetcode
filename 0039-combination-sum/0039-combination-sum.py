class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)

        def backtracking(start,current):
            if sum(current) == target:
                result.append(current[:])
                return
            elif sum(current) >= target:
                return

            for i in range(start,n):
                current.append(candidates[i])
                backtracking(i,current)
                current.pop()

        backtracking(0,[])


        return result