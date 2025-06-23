class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = nums.count(0)
        result = []
        total = 1

        if zero >1:
            return [0] *len(nums)
        elif zero == 1:
            for i in nums:
                if i != 0 :
                    total *= i
            
            for i in nums:
                if i == 0:
                    result.append(total)
                else:
                    result.append(0)

        else:
            for i in nums:
                total *= i
            
            for i in nums:
                result.append(total//i)
        return result