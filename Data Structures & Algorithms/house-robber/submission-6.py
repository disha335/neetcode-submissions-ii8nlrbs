class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        # memo = [-1]*n
        # def helper(i):
        #     if i==0:
        #         # not picked up ind=1
        #         return nums[i]
        #     if i<=0:
        #         return 0
        #     if memo[i]!=-1:
        #         return memo[i]
        #     pick = nums[i]+helper(i-2)
        #     notPick = helper(i-1)
        #     memo[i] = max(pick,notPick)
        #     return memo[i]
        # return helper(n-1)

        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=nums[0]
        for i in range(2,n+1):
            pick = nums[i-1]+dp[i-2]
            notPick = dp[i-1]
            dp[i]=max(pick,notPick)
        return dp[n]