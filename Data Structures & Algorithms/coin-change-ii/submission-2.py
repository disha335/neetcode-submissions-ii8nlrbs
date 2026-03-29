class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # memo = {}
        # def helper(amount, i):
        #     if amount == 0:
        #         return 1
            
        #     if amount<0 or i>=len(coins):
        #         return 0 
            
        #     if (amount, i) in memo:
        #         return memo[(amount, i)]
                
        #     exclude = helper(amount, i+1)
        #     include = helper(amount-coins[i], i)
        #     memo[(amount, i)] = exclude+include
        #     return memo[(amount, i)]
        # return helper(amount, 0)

        dp = [0]*(amount+1)
        dp[0]=1

        for coin in coins:
            for x in range(coin, amount+1):
                dp[x]+=dp[x-coin]
        return dp[amount]