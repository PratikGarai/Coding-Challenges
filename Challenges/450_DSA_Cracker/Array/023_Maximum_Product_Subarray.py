#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		mx = -100
		pr = 1
		left, right = 0, 0
		
		mele = -100
		for i in arr :
		    mele = max(i, mele)

		while right < n : 
		    if arr[right] == 0 :
		        while left < right-1 :
		            pr = pr//arr[left]
		            mx = max(mx, pr)
		            left += 1
	            right += 1
	            left = right
	            pr = 1
            else : 
                pr = pr * arr[right]
                right += 1
                mx = max(mx, pr)
        while left < right-1 : 
            pr = pr//arr[left]
            mx = max(mx, pr)
            left += 1
        return max(mx, mele)


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
