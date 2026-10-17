class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(i,nums):
            n=len(nums)
            dp = [0]*(n+1)
            dp[0]=0
            dp[1]=nums[0]
            for i in range(2,n+1):
                pick = nums[i-1]+dp[i-2]
                noPick = dp[i-1]
                dp[i] = max(pick,noPick)
            return dp[n]
        if len(nums)==1:
            return nums[0]
        return max(helper(len(nums)-2,nums[1:]),helper(len(nums)-2,nums[:-1]))