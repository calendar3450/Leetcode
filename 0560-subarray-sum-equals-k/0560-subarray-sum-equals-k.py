class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0:1}
        result = 0
        current = 0

        for i in nums:
            current += i 
            result += count.get(current-k,0)
            count[current] = count.get(current,0)+1

        return result
        
