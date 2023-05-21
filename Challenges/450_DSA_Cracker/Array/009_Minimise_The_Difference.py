#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        arr = sorted(arr)
        n = len(arr)
        mi = arr[0]
        ma = arr[n-1]
        ans = ma - mi
        for i in range(1, n):
            if arr[i] - k < 0:
                continue
            mi = min(arr[0] + k, arr[i] - k)
            ma = max(arr[i-1] + k, arr[n-1] - k)
            ans = min(ans, ma - mi)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
