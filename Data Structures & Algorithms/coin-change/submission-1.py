class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def helper(amount):
            if amount==0:
                return 0

            if amount<0:
                return float("inf")

            if amount in memo:
                return memo[amount]

            mini = float("inf")
            for coin in coins:
                ans = helper(amount-coin)
                if ans!=float("inf"):
                    mini = min(mini, ans+1)
                    memo[amount] = mini
            return mini

        res = helper(amount)
        return res if res!=float("inf") else -1