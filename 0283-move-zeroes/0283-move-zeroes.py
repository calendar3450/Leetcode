class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n= len(nums) 
        cnt_zero = nums.count(0)
        j=0
        i=0
        if n == 1 and nums[0] == 0:
            return nums

        while i <n and j<cnt_zero:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                j+=1
            else:
                i+=1

        return nums