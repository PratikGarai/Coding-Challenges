class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A)
        arr = [ [] for i in range((n*2)-1)]

        for i in range(n) :
            for j in range(n) :
                arr[i+j].append(A[i][j])
        
        return arr
