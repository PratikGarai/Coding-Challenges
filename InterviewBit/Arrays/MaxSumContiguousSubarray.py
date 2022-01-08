class Solution:
    # @param a : tuple of integers
    # @return an integer
    def maxSubArray(self, a):

        mx = -10000
        mn = -10000
        l = len(a)
        dp = [0 for i in range(l)]
        
        for i in range(l) :
            dp[i] = max(0, dp[i-1]+a[i])
            mx = max(dp[i], mx)
            mn = max(mn, a[i])

        if mn <= 0 :
            return mn 
        return mx
