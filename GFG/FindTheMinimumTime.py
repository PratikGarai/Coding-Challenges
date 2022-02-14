#User function Template for python3

class Solution:
    
    def minTime(self, s1, s2, N):
        
        if s2<s1 :
            s1, s2 = s2, s1
        mc = s2*N

        def getCost(ind) :
            return max(s1*ind, (N-ind)*s2)
            
        left = 0
        right = N
        while(left <= right) :
            mid = (left+right)//2
            mc = min(mc, getCost(mid))
            if mid*s1 > (N-mid)*s2:
                right = mid -1
            else : 
                left = mid + 1 

        return mc

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S1, S2, N = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.minTime(S1, S2, N))
# } Driver Code Ends
