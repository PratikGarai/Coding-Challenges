class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        l = len(A)
        sm = sum(A[:B])
        mx = sm

        for i in range(B) :
            sm = sm - A[B-i-1] + A[l-i-1]
            mx = max(mx, sm)
        
        return mx
