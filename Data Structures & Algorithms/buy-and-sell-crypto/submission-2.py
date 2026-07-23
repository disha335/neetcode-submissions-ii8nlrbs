class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxP = 0
        for i in range(n-1):
            buy=prices[i]
            for j in range(i+1, n):
                sell=prices[j]
                maxP = max(maxP, sell-buy)
        return maxP
