class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        # memo = {}
        # def helper(i1, i2):
        #     if i1>= m or i2>= n:
        #         return 0
        #     if (i1, i2) in memo:
        #         return memo[(i1, i2)]
        #     if text1[i1]==text2[i2]:
        #         return 1+helper(i1+1, i2+1)
        #     memo[(i1, i2)] = max(helper(i1+1, i2), helper(i1, i2+1))
        #     return memo[(i1, i2)]
        # return helper(0, 0)
        dp = [[0 for i in range(m+1)] for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1, m+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        return dp[n][m]
