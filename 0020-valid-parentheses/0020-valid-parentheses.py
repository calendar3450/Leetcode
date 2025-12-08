class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mappings = {')' : '(', '}': '{', ']':'['}

        for char in s:
            if char in mappings:
                if stack:
                    top = stack.pop()
                else:
                    top = '1'

                if top != mappings[char]:
                    return False
            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False