#User function Template for python3

class Solution:
    
    def __init__(self) :
        self.radix = 10E7
    
    def get(self, arr, ind, original = True) :
        if original : 
            return arr[ind] % self.radix
        else : 
            return arr[ind] // self.radix
            
    def modifyAndStore(self, arr1, arr2, n, m, ind, val) : 
        if ind < n : 
            arr1[ind] = (val*self.radix) + arr1[ind]
        else : 
            arr2[ind-n] = (val*self.radix) + arr2[ind-n]
    
    def merge(self,arr1,arr2,n,m):
        
        i = 0
        j = 0
        ind = 0
        
        while i<n and j<m : 
            if self.get(arr1, i) < self.get(arr2, j) : 
                self.modifyAndStore(arr1, arr2, n, m, ind, self.get(arr1, i))
                i += 1
                ind += 1
            else :
                self.modifyAndStore(arr1, arr2, n, m, ind, self.get(arr2, j))
                j += 1
                ind += 1
        
        while i<n :
            self.modifyAndStore(arr1, arr2, n, m, ind, self.get(arr1, i))
            i += 1
            ind += 1
        
        while j<m :
            self.modifyAndStore(arr1, arr2, n, m, ind, self.get(arr2, j))
            j += 1
            ind += 1
            
        for i in range(n) : 
            arr1[i] = int(self.get(arr1, i, False))
        for i in range(m) : 
            arr2[i] = int(self.get(arr2, i, False))
        


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
# } Driver Code Ends
