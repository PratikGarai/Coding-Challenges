class Solution:
    # @param A : list of integers
    # @return an integer
    def divisibleBy60(self, A):

        d = {}

        if len(A) == 1 :
            if A[0]==0 :
                return 1
            return 0

        for i in A : 
            if i in d : 
                d[i] += 1
            else :
                d[i] = 1
        
        if 0 not in d :
            return 0
        
        if (2 not in d) and (4 not in d) and (6 not in d) and (8 not in d) :
            return 0

        su = 0
        for k,v in d.items() :
            su += k*v
        
        if su%3==0 :
            return 1
        return 0
