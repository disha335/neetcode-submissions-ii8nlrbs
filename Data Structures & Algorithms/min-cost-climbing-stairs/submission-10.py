class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        # memo={0:0,1:0}
        # def helper(i):
        #     if i in memo:
        #         return memo[i]
        #     twoStep=float("inf")
        #     oneStep = helper(i-1)+cost[i-1]
        #     if i>1:
        #         twoStep = helper(i-2)+cost[i-2]
        #     memo[i] = min(oneStep,twoStep)
        #     return memo[i]
        # return helper(n)

        n=len(cost)
        dp = [0]*(n+1)
        for i in range(2,n+1):
            twoStep=float("inf")
            oneStep = dp[i-1]+cost[i-1]
            if i>1:
                twoStep = dp[i-2]+cost[i-2]
            dp[i] = min(oneStep,twoStep)
        return dp[n]    
        
        
