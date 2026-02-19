class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        tmp = -9999999999
        tmpLeng = 0

        for i in nums:

            if tmp +1 == i:
                tmpLeng +=1

            elif tmp == i:
                continue
                
            else:
                ans = max(ans,tmpLeng)
                tmpLeng = 1

            tmp = i

        return max(ans,tmpLeng)