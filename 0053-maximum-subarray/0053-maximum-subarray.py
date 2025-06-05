class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result_DP = [0] *(len(nums))
        result_DP[0] = nums[0]

        for i in range(1,len(nums)):
            result_DP[i] = max(0,result_DP[i-1]+nums[i])

        return max(result_DP)