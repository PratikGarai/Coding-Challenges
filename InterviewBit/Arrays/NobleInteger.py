class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        A = sorted(A)
        l = len(A)
        A.append(A[-1]+1)

        for i in range(l):
            if A[i]==l-i-1 and A[i]!=A[i+1]:
                return 1

        return -1
