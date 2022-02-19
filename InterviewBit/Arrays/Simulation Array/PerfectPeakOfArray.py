class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):

        l = len(A)
        d = [False for i in range(l)]

        mx = A[0]
        for i in range(1, l-1) :
            if A[i]>mx :
                d[i] = True
                mx = A[i]
        
        mn = A[l-1]
        for i in range(l-2, 0, -1) :
            if A[i]<mn :
                if d[i] :
                    return 1
                else : 
                    mn = A[i]
        
        return 0
