class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.lstrip()          # 1. 앞 공백 제거
        if not s:
            return 0
        
        sign = 1
        idx = 0
        
        # 2. 부호 처리
        if s[0] == '-':
            sign = -1
            idx = 1
        elif s[0] == '+':
            idx = 1
        
        # 3. 숫자만 읽기
        num = 0
        while idx < len(s) and s[idx].isdigit():
            num = num * 10 + int(s[idx])
            idx += 1
        
        num *= sign
        
        # 4. 32비트 범위 클램핑
        INT_MIN = -2**31       # -2147483648
        INT_MAX = 2**31 - 1    #  2147483647
        
        return max(INT_MIN, min(INT_MAX, num))