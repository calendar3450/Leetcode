class Solution:
    def reverse(self, x: int) -> int:
        minus = False

        if x<0:
            minus = True
            x *= -1

        x_str_reverse = str(x)[::-1]

        if minus:
            x_int_reverse = int(x_str_reverse) * -1
        else:
             x_int_reverse = int(x_str_reverse)

        if x_int_reverse>=2**31-1 or x_int_reverse< -2**31:
            return 0
        
        else:
            return x_int_reverse