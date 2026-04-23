from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tmp = Counter(nums)
        
        for i in tmp:
            if tmp[i] >1:
                return True
        
        return False