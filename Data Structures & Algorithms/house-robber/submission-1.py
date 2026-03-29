class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def helper(i):
            if i>=n:
                return 0
            if i in memo:
                return memo[i]
            one = nums[i] + helper(i+2)
            two = helper(i+1)
            memo[i] = max(one,two)
            return memo[i]
        return helper(0)