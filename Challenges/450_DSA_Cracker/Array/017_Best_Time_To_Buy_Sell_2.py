class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = 0
        n = len(prices)
        for i in range(0, n-1) : 
            if prices[i] < prices[i+1] : 
                profits += prices[i+1] - prices[i]
        return profits
