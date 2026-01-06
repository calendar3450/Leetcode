class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * (n+1)
        dp[0] = nums[0]

        if 0 not in nums:
            return True
        elif n==1:
            return True
        elif nums[0] == 0 and n>1:
            return False

        for i in range(1,n):
            dp[i] = max(dp[i-1], i+nums[i])

            if dp[i] >=n-1:
                return True
            if dp[i] == i:
                return False