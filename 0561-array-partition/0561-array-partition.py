class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        nums.sort()

        for i in range(0,n,2):
            total += min(nums[i],nums[i+1])
        return total