class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = sorted(list(s))
        tList = sorted(list(t))
        if sList == tList:
            return True
        else:
            return False