class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = 10000
        maxProfit = 0
        for i in prices : 
            minBuy = min(i, minBuy)
            maxProfit = max(maxProfit, i-minBuy)
        return maxProfit
