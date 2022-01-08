class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):

        l = [0 for i in range(B)]
        le = len(A)

        mx = B
        mi = 1
        for i in range(le-1, -1, -1) :
            if A[i]=="I":
                l[i+1] = mx
                mx -= 1
            else :
                l[i+1] = mi
                mi += 1
        
        l[0] = mi
        return l
