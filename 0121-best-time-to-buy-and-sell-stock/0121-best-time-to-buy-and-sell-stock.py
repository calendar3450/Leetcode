class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        result =[0]*len(prices)

        for i in range(1,len(prices)):
            result[i] = max(result[i-1],prices[i]-buy)
            buy = min(buy, prices[i])

        return result[-1]