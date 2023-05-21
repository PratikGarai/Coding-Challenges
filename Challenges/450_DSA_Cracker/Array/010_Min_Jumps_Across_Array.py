#User function Template for python3
class Solution:
    def minJumps(self, arr, n):
        steps = 1
        step_index = 0
        reach = step_index+arr[step_index]
        
        while (reach+1) <= n :
            mx = 0
            mxind = -1
            for i in range(step_index+1, reach+1) :
                if i+arr[i] > mx : 
                    mx = i+arr[i]
                    mxind = i
            if mx <= reach :
                return -1
            if reach+1 >= n : 
                break
            else : 
                # print("Step {} from {}. Reach = {}".format(arr[mxind], mxind, reach))
                steps += 1
                step_index = mxind
                reach = step_index + arr[step_index]
        
        return steps


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends
