class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        result = ''
        

        for i in range(len(s)):
            for j in range(i+1,len(s)):
                tmp = s[i:j]

                if tmp == tmp[::-1]:
                    if len(result) < len(tmp):
                        result = tmp
                

        return result