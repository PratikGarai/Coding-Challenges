class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        if B==1 :
            return A
        res = ""
        l = len(A)
        matrix = [[-1 for i in range(l)] for j in range(B)]
        inc = True
        ind = 0
        for i in range(l):
            if ind==0 : 
                inc = True
            if ind==B-1 :
                inc = False
            matrix[ind][i] = A[i]
            if inc : 
                ind += 1
            else :
                ind -= 1
        
        for j in range(B):
            for i in range(l):
                if matrix[j][i] != -1 :
                    res += matrix[j][i]
        
        return res
