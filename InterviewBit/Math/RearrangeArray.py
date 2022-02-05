class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):

        n = len(A)
        for i in range(n) :
            if A[A[i]]>=n :
                A[i] = ((A[i]+1)*n) + ((A[A[i]]//n)-1)
            else : 
                A[i] = ((A[i]+1)*n) + A[A[i]]

        for i in range(n) :
            A[i] = A[i]%n 
        return A
