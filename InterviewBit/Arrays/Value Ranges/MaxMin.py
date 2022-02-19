class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        mx = -(10**9+1)
        mi = 10**9+1

        for i in A :
            if i<mi :
                mi = i
            if i>mx :
                mx = i
        
        return mi+mx
