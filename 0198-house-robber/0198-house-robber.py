class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        one_before = 0
        two_before = 0

        for num in nums:
            cur_val = max(one_before, two_before + num)
            one_before,two_before = cur_val, one_before

        result_fir = one_before

        one_before = 0
        two_before = 0

        for num in nums[1:]:
            cur_val = max(one_before, two_before + num)
            one_before,two_before = cur_val, one_before

        result_sec = one_before

        return max(result_fir,result_sec)
