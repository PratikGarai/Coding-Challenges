class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):

        l = len(A)
        mx = max(A)

        if mx<=0 :
            return 1

        f = [False for i in range(mx+1)]

        for i in A : 
            if i>0 :
                f[i] = True
        
        for i in range(1, mx+1) :
            if not f[i] :
                return i
        
        return mx+1
