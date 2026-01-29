class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n= len(s)

        # dp[i-2], dp[i-1]
        dp = [0] *(n+1)
        dp[0] ,dp[1] =1,1
        

        for i in range(2, len(s) + 1):
            one = s[i-1]          # 한 자리
            two = s[i-2:i]        # 두 자리

            if one != '0':
                dp[i] += dp[i-1]

            if '10' <= two <= '26':
                dp[i] += dp[i-2]

        return dp[n]