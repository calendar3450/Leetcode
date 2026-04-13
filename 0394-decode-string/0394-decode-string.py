class Solution:
    def decodeString(self, s: str) -> str:
        num= []
        strings= []
        st = ''
        cur_num = 0

        for i in s:
            if i.isdigit():
                cur_num += cur_num * 10 + int(i)
            
            elif i == '[':
                num.append(cur_num)
                strings.append(st)
                st = ''
                cur_num = 0

            elif i == ']':
                n = num.pop()
                s = strings.pop()
                st = s + st*n

            else:
                st += i
        
        return st

