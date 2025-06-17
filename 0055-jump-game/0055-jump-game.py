class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current = 0 
        far = 0

        if len(nums) ==1 or 0 not in nums:
            return True
            
        elif nums[0]==0:
            return False

        for i in range(len(nums)):
            far = max(i+nums[i],far)
            if current == i:
                current = far
                if current >=len(nums)-1:
                    return True
        return False

                