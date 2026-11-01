from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        answer = []
        check = len(nums) // 3
        numCounter = Counter(nums)
        
        for i in numCounter:
            if numCounter[i] >check:
                answer.append(i)

        return answer