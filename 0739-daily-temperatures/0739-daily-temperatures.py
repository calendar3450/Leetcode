class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                result[j] = i-j

            stack.append(i)    

        return result
                