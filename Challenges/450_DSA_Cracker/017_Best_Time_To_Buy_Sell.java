class Solution {
    public int maxProfit(int[] prices) {
        int buy = Integer.MAX_VALUE;
        int l = prices.length;
        int maxProfit = 0, profit;

        for(int i=0; i<l; i++) {
            buy = Math.min(buy, prices[i]);
            profit = prices[i] - buy;
            maxProfit = Math.max(profit, maxProfit);
        }

        return maxProfit;
    }
}
