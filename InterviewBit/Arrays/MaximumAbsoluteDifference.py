class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):

        l = len(A)
        res1 = [A[i]+i for i in range(l)]
        res2 = [A[i]-i for i in range(l)]
        res1 = sorted(res1)
        res2 = sorted(res2)

        return max(res1[-1]-res1[0],res2[-1]-res2[0])
