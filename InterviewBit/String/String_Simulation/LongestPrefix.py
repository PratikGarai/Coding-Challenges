class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):

        l = len(A[0])
        mx = A[0]
        for i in A : 
            le = len(i)
            if le<l : 
                l = le
                mx = i 
        
        for i in range(l) :
            for j in A :
                if j[i]!=mx[i]:
                    return mx[:i]

        return mx
