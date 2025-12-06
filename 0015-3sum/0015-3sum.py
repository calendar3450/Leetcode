class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()


        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break

            l, r = i+1, len(nums)-1
            while l<r:
                if nums[i] + nums[l] + nums[r] == 0:
                    result.append([nums[i],nums[l],nums[r]])
                    l+=1
                elif nums[i] + nums[l] + nums[r] <0:
                    l+=1
                else:
                    r-=1
        
        result = list({tuple(x) for x in result})

        return result