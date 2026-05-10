class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        for i in s:
            if i.isalpha():
                stack_s.append(i)
            elif stack_s and not i.isalpha():
                stack_s.pop()

        for i in t:
            if i.isalpha():
                stack_t.append(i)
            elif stack_t and not i.isalpha():
                stack_t.pop()

        if stack_s == stack_t:
            return True
        else:
            return False
