class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n

        for idx,tem in enumerate(temperatures):
            while stack and temperatures[stack[-1]] <tem:
                j = stack.pop()
                result[j] = idx - j

            stack.append(idx)

        return result