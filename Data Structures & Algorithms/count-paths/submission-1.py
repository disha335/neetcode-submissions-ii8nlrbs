class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {(m-1, n-1): 1}
        def helper(i, j):
            if i<0 or j<0 or i>=m or j>=n:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i, j)] = helper(i+1, j)+helper(i, j+1)
            return memo[(i, j)]
        return helper(0, 0)