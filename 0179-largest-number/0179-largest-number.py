class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        a = sorted(nums,key=lambda x : str(x)*9,reverse=True)
        ans = ''

        for i in a:
            ans+=str(i)

        if int(ans)==0:
            return '0'
        else:
            return ans