# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l ,r = 1, n
        if n == 1:
            return 1

        while l<=r:
            mid = (l+r) //2

            if isBadVersion(mid) == True and isBadVersion(mid -1) == True:
                r = mid -1
            elif isBadVersion(mid) == False and isBadVersion(mid -1) == False:
                l = mid +1
            else: 
                return mid
