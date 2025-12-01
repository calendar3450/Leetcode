class Solution:
    def reverse(self, x: int) -> int:

        a = str(abs(x))

        if x<0:
            b= '-'
        else:
            b=''

        for i in range(len(a)-1,-1,-1):
            b+=a[i]
            
        if int(b) > 2**31-1:
            return 0
        elif int(b) < (-2)**31:
            return 0
        else:
            return int(b)
        