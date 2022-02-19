class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n= len(A)
        md = 10**9 + 7

        return ((2**n)-1)%md
