class Solution:
    def decodeString(self, s: str) -> str:
        int_stack = []
        str_stack = []
        tmp_int = 0
        tmp_str = ''

        for i in s:
            if i.isdigit():
                tmp_int = tmp_int *10+int(i)
                
            elif i =='[':
                int_stack.append(tmp_int)
                str_stack.append(tmp_str)
                tmp_int = 0
                tmp_str = ''
            elif i == ']':
                repeat_int = int_stack.pop()
                repeat_str = str_stack.pop()
                tmp_str = repeat_str + tmp_str *repeat_int
            else:
                tmp_str +=i
        
        return tmp_str