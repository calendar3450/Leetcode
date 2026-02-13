class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = prices[0]
        n = len(prices)

        for i in range(1,n):
            if buy > prices[i]:
                buy = prices[i]

            else:
                if ans< prices[i] - buy:
                    ans = prices[i] - buy

        return ans


