class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        # def func(i,target):
        #     if i==0:
        #         if target%coins[0]==0:
        #             return target//coins[0]
        #         else:
        #             return float("inf")
        #     notTake = func(i-1,target)
        #     take=float("inf")
        #     if target>=coins[i]:
        #         take=1+func(i,target-coins[i])
        #     return min(take,notTake)
        # ans = func(n-1,amount)
        # if ans==float("inf"):
        #     return -1
        # return ans
        dp =[[0]*(amount+1) for _ in range(n)]
        for t in range(amount+1):
            if t%coins[0]==0:
                dp[0][t]=t//coins[0]
            else:
                dp[0][t]=float("inf")
        for i in range(1,n):
            for t in range(amount+1):
                notTake=dp[i-1][t]
                take=float("inf")
                if t>=coins[i]:
                    take=1+dp[i][t-coins[i]]
                dp[i][t]=min(take,notTake)
        return dp[n-1][amount] if dp[n-1][amount]!=float("inf") else -1
