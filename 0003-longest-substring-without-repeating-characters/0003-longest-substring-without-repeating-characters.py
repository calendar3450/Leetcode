class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        left,right = 0,0
        while left<len(s) and right <len(s):
            tmp=s[left:right]
            if s[right] in tmp:
                left +=1
                if left>right:
                    right+=1
            else:
                right +=1

            result = max(result, right-left)
            
        return result