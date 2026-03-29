class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def helper(i):
            # Base Case
            if i>=n:
                return 0
            if i in memo:
                return memo[i]
            # Recurrence Relation
            oneCost = cost[i] + helper(i+1)
            twoCost = cost[i] + helper(i+2)
            memo[i] = min(oneCost, twoCost)
            return memo[i]
        return min(helper(0), helper(1))
        # TC -> O(2^n)

        # DP
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 0
        # 0 0 2 4
        for i in range(2, n+1):
            one = cost[i-1]+dp[i-1]
            two = cost[i-2]+dp[i-2]
            dp[i] = min(one, two)
        return dp[n]
