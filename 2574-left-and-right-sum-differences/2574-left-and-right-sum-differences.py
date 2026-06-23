class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = []
        right_sum = []
        result = []
        n = len(nums)
        cur_sum = 0

        for i in range(n):
            left_sum.append(cur_sum)
            cur_sum += nums[i]

        cur_sum = 0

        for i in range(n-1,-1,-1):
            right_sum.append(cur_sum)
            cur_sum += nums[i]
        
        right_sum = right_sum[::-1]
        
        for i in range(n):
            result.append(abs(right_sum[i]-left_sum[i]))

        return result