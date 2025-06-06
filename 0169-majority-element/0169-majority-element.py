class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_list = list(set(nums))
        max = 0
        result = 0
        if len(nums_list) == 1:
            return nums_list[0]
        for i in nums_list:
            if nums.count(i) >max:
                max = nums.count(i)
                result = i

        return result