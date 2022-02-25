class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        mat = [[0 for i in range(A)] for j in range(B)]
        for i in range(B) :
            mat[i][0] = 1
        for i in range(A) :
            mat[0][i] = 1
        for i in range(1, B):
            for j in range(1, A):
                mat[i][j] = mat[i-1][j]+mat[i][j-1]    
        return mat[B-1][A-1]
