class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp = [False] *(n+1)
        dp[0] = True
        check = ''

        for i in range(1,n+1):
            for j in range(i):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True

        if dp[n]:
            return True
        else:
            return False
