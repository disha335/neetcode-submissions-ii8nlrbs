class Solution:
    def tribonacci(self, n: int) -> int:
        memo={0:0,1:1,2:1}
        def helper(i):
            if i in memo:
                return memo[i]
            memo[i] = helper(i-1)+helper(i-2)+helper(i-3)
            return memo[i]
        return helper(n)