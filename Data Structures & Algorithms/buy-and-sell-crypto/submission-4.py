class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit=0
        for r in range(len(prices)):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxProfit=max(profit, maxProfit)
            else:
                l=r
        return maxProfit