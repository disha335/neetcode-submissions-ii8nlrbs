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