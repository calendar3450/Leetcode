class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0:-1}
        ans = 0
        cnt = 0

        for i in range(len(nums)):
            if nums[i] ==1:
                cnt+=1
            else:
                cnt -=1
            
            if cnt in dic:
                ans = max(ans,i-dic[cnt])
            else:
                dic[cnt] = i


        return ans
