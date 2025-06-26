class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        result = 9999999
        for i in nums:
            if abs(result) >abs(i-0):
                result = i
            elif abs(result) == abs(i):
                if result < i:
                    result = i
            
        return result