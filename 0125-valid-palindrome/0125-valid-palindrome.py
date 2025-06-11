class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s =='':
            return True
        
        s = re.sub(r"[^A-Za-z0-9]", "", s)
        s=s.lower()

        if s[::-1]==s:
            return True
        else:
            return False