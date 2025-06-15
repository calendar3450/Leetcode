class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        num = 0
        sign = 1
        stack =[]

        for ch in s:
            if ch.isdigit():
                num = num*10 +int(ch)
            elif ch == '+':
                res +=sign *num
                num = 0
                sign = 1
            elif ch =='-':
                res +=sign *num
                num = 0
                sign =-1
            elif ch =='(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign =1
            elif ch==')':
                res += sign * num
                num = 0
                prev_sign = stack.pop()
                prev_res = stack.pop()
                res = prev_res + prev_sign *res

        res += sign * num
        return res