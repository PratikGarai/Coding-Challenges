/*
Since we can buy or sell on any day, we scan and store the lowest price and compare it to all subsequent prices.
*/
class Solution {
    public int maxProfit(int[] prices) {
        int min = prices[0];
        int max_profit = 0;
        for(int i:prices) {
            max_profit = Math.max(max_profit, i-min);
            min = Math.min(min, i);
        }
        return max_profit;
    }
}