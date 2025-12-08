class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        result = 0
        dic = {0:-1}
        prefix = 0

        for i,num in enumerate(nums):
            prefix +=1 if num == 1 else -1

            if prefix in dic:
                result = max(result, i-dic[prefix])

            else:
                dic[prefix] = i

            

        return result   
