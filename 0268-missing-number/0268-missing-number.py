class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        check = nums[0]
        if check != 0:
            return 0
        
        for i in nums:
            if i != check:
                return check
            check +=1

        return check