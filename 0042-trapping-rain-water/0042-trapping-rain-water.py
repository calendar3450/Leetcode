class Solution:
    def trap(self, height: List[int]) -> int:
        n= len(height)
        if n <= 2:
            return 0
        left = 0
        right = n-1
        result = 0
        leftMax = [0]*n
        rightMax = [0]*n

        leftMax[0] = height[0]
        for i in range(n):
            leftMax[i]= max(height[i],leftMax[i-1])

        rightMax[n-1] = height[n-1]
        for j in range(n-2,-1,-1):
            rightMax[j] = max(height[j],rightMax[j+1])

        for i in range(n):
            result += min(rightMax[i],leftMax[i])-height[i]

        return result

        
