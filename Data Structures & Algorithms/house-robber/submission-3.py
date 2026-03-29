class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # memo = {}
        # def helper(i):
        #     if i>=n:
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     one = nums[i] + helper(i+2)
        #     two = helper(i+1)
        #     memo[i] = max(one,two)
        #     return memo[i]
        # return helper(0)
        dp = [0]*n
        dp[0] = nums[0]
        if n>1:
            dp[1] = max(nums[0], nums[1])
        if n>2:
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]