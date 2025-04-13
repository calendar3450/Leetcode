class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right:int) -> str:
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        result= ''
        if len(s)<2:
            return s
        else:
            for i in range(len(s)-1):
                result= max(expand(i,i+1),expand(i,i+2),result,key=len)

        return result


        return answer
        