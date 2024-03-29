class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):

        A = sorted(A)
        l = len(A)
        
        for i in range(l//2):
            A[2*i], A[2*i+1] = A[2*i+1], A[2*i]

        return A
