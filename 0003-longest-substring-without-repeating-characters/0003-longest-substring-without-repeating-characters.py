class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        record = 0

        for i in s:
            if i in substring:
                record = max(record, len(substring))
                substring = i
            else:
                substring +=i

        record = max(record, len(substring))
        
        return record