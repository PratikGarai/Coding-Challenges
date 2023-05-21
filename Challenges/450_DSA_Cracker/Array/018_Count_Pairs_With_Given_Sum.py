#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        s = {}
        for num in arr :
            if num in s :
                s[num] += 1
            else : 
                s[num] = 1
        
        c = 0
        for num in s :
            d = k-num
            if d in s :
                if num == d : 
                    c += (s[num] * (s[d] - 1))//2
                else : 
                    c += s[num] * s[d]
                s[num] = 0
                s[d] = 0
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
