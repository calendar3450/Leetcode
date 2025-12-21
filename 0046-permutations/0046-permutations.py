class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        
        def backtracking(cur):
            if len(cur) == n:
                result.append(cur.copy())
                return
            
            for i in nums:
                if i not in cur:
                    cur.append(i)
                    backtracking(cur)
                    cur.pop()

        backtracking([])

        return result