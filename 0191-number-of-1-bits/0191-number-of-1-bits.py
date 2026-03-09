class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_only = format(n, 'b')  # '1010'

        ans =0
        
        for i in binary_only:
            if i == '1':
                ans+=1

        return ans