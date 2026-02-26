class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]* (n+1)
        dp[0] = True 
        for i in range(n+1):
            for j in range(i):
                tmp = s[j:i]
                if tmp in wordDict and dp[j]:
                    dp[i] = True
                    break
        
        return dp[n]