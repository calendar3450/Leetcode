class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        result = []

        def backtracking(sublist):
            if sublist in result:
                return

            if len(sublist)==len(nums):
                result.append(sublist.copy())
                return

            for i in nums:
                if i not in sublist:
                    sublist.append(i)
                    backtracking(sublist)
                    sublist.pop()

        for j in nums:
            sublist=[j]
            backtracking(sublist)

        return result                    
            