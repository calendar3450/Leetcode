class Solution:
    def reverse(self, x: int) -> int:

        s= abs(x)
        sList = list(str(s))[::-1]
        result = 0
        for i in sList:
            result =(result *10)+int(i)
        if x <0:
            result*=-1
        if result <(-2**31) or result > (2**31)-1:
            return 0
        return result