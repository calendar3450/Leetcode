from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_set = Counter(nums)
        ans = 0
        ans_cnt = 0

        for i in nums_set:
            if ans_cnt < nums_set[i]:
                ans = i
                ans_cnt = nums_set[i]
        

        return ans
