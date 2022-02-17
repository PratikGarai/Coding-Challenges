class Solution:
    # @param A : list of integers
    # @return a list of integers
    def findOccurences(self, A):

        d = {}
        for i in A : 
            if i in d :
                d[i] += 1
            else :
                d[i] = 1
        
        d = sorted(list(d.items()))
        res = []
        for i in d : 
            res.append(i[1])
        return res
