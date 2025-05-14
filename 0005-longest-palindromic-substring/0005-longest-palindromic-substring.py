class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) ==1 or s==s[::-1]:
            return s
        result = ''
        forward = ''
        sReverse = s[::-1]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                forward = s[i:j]
                if forward == forward[::-1] and len(forward)>= len(result):
                    result = forward
        
        return result