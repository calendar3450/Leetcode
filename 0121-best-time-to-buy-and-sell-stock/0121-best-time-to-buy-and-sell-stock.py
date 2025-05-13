class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        buy =prices[0]

        if len(prices) == 1:
            return 0

        for i in range(1,len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            elif total < prices[i] - buy:
                total= prices[i] - buy

        if total<0:
            return 0
        else:
            return total

