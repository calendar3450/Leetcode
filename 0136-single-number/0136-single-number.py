from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        
        for i in cnt:
            if cnt[i] == 1:
                return i