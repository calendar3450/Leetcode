class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0:1}
        current_sum = 0
        result = 0

        for num in nums:
            current_sum += num
            result += count.get(current_sum - k,0)
            count[current_sum] = count.get(current_sum,0) + 1
            

        return result
        
