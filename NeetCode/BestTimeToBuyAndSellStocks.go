/*
	Go over the array. Store the min till now. Compare the min till now to the current value.
	That'll give the max profit.
*/

package main

func maxProfit(prices []int) int {
	var maxProfit, globalMin, l int = 0, 10e5, len(prices)

	for i := 0; i < l; i++ {
		if prices[i] < globalMin {
			globalMin = prices[i]
		}
		if maxProfit < (prices[i] - globalMin) {
			maxProfit = prices[i] - globalMin
		}
	}

	return maxProfit
}
