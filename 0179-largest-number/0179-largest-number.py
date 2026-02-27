class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key =lambda x: str(x) *9, reverse=True)
        answer = ''
        for i in nums:
            answer +=str(i)
        
        if int(answer) == 0:
            answer = '0'
        
        return answer