class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s=s.replace(' ','')
        num= 0
        lastOperation = '+'

        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])

            if not s[i].isdigit() or i == len(s)-1:
                if lastOperation =='+':
                    stack.append(num)
                elif lastOperation == '-':
                    stack.append(-num)
                elif lastOperation == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop()/num))
                
                num=0
                lastOperation=s[i]

        return sum(stack)