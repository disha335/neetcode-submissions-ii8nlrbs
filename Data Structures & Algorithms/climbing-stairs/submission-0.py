class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(n):
            if n<=1:
                return 1
            return helper(n-1)+helper(n-2)
        return helper(n)
        