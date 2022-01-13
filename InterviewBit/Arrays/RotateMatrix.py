class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        l = len(A)
        mid = l//2
        for i in range(mid):
            for j in range(mid):
                t = A[i][j]
                A[i][j] = A[l-1-j][i] 
                A[l-1-j][i] = A[l-1-i][l-1-j] 
                A[l-1-i][l-1-j] = A[j][l-1-i]
                A[j][l-1-i] = t

        if l%2==1:
            i = mid
            for j in range(mid):
                t = A[i][j]
                A[i][j] = A[l-1-j][i] 
                A[l-1-j][i] = A[l-1-i][l-1-j] 
                A[l-1-i][l-1-j] = A[j][l-1-i]
                A[j][l-1-i] = t

        return A
