class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # def helper(i):
        #     n=len(cost)
        #     memo=[-1]*(n+1)
        #     if i==0 or i==1:
        #         return 0
        #     if memo[i]!=-1:
        #         return memo[i]
        #     fs = cost[i-1]+helper(i-1)
        #     ss = cost[i-2]+helper(i-2)
        #     memo[i] = min(fs,ss)
        #     return memo[i]
        # return helper(len(cost))

        n=len(cost)
        dp=[0]*(n+1)
        prev2=0
        prev=0
        for i in range(2,n+1):
            fs = cost[i-1]+prev
            ss = cost[i-2]+prev2
            curr = min(fs,ss)
            prev2=prev
            prev=curr
        return prev