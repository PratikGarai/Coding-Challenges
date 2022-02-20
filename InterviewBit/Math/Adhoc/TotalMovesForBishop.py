class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return min(A-1, B-1) + min(A-1, 8-B) + min(8-A, B-1) + min(8-A, 8-B)
