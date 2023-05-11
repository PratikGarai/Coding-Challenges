#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        
        sumHere = 0
        maxSum = 0
        maxEle = -10E7
        
        for i in range(N) :
            maxEle = max(maxEle, arr[i])
            sumHere += arr[i]
            maxSum = max(maxSum, sumHere)
            sumHere = max(0, sumHere)
        
        if(maxEle < 0) :
            return maxEle
        else : 
            return maxSum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
