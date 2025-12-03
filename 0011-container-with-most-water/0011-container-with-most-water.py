class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        result = 0

        while l <= r:
            tmp = min(height[l],height[r]) * (r-l)
            if tmp > result:
                result = tmp
            
            if height[l] > height[r]:
                r-=1
            else:
                l+=1

        return result