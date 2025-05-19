class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # result = 0
        # prefix_sum = [0]*(len(nums)+1)
        
        # for i in range(1,len(nums)+1):
        #     prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

        # for i in range(len(nums),-1,-1):
        #     for j in range(i):
        #         if prefix_sum[i]-prefix_sum[j]==k:
        #             result +=1
    

        count = {0:1}
        current_sum = 0
        result = 0

        for num in nums:
            current_sum += num
            result += count.get(current_sum - k,0)
            count[current_sum] = count.get(current_sum,0) + 1
            

        return result
        
