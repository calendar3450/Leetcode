class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur_result = -999999
        max_result = -999999

        for i in nums:
            cur_result = max(cur_result + i, i)
            max_result = max(max_result, cur_result)
        
        return max_result
        