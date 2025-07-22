class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result =[]
        tmp = []

        def backtracking(start):
            
            result.append(tmp.copy())

            for i in range(start,len(nums)):
                tmp.append(nums[i])
                backtracking(i+1)
                tmp.pop()

        backtracking(0)

        return result