#User function Template for python3

class Solution:
    def getIndex(self, a, b, c) :
        if a<=b and a<=c : 
            return 0
        if b<=a and b<=c :
            return 1
        else :
            return 2
    
    def commonElements (self,A, B, C, n1, n2, n3):
        aux = set()
        res = []
        i, j, k = 0, 0, 0
        while i<n1 and j<n2 and k<n3 : 
            if A[i]==B[j] and B[j]==C[k]:
                if A[i] not in aux:
                    res.append(A[i])
                    aux.add(A[i])
                if i<n1 : 
                    i += 1
                if j<n2:
                    j += 1
                if k<n3 :
                    k += 1
            else :
                ele = self.getIndex(A[i], B[j], C[k])
                if ele == 0 :
                    i += 1
                elif ele == 1:
                    j += 1
                else :
                    k += 1
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends
