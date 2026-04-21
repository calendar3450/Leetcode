from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []

        for i in s:
            if not stack and i == " ":
                continue
            
            elif stack and i == " " and stack[-1] !=' ':
                stack.append(i)
            
            elif i.isalpha() or i.isdigit():
                stack.append(i)

        if stack[-1] == ' ':
            stack.pop()

        ans = ''
        stack2 = []
        tmp = ''

        for i in stack:
            if i == ' ':
                stack2.append(tmp)
                stack
                tmp = ''
            else:
                tmp += i

        if tmp != '':
            stack2.append(tmp)

        n = len(stack2)

        for _ in range(n-1):
            ans+=stack2.pop()
            ans += ' '
        
        ans += stack2.pop()

        return ans
