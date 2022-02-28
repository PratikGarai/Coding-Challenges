class Solution:
    # @param A : string
    # @return a list of integers
    def solve(self, A):
        res = {}
        mem = []
        for i in A :
            if i in res :
                res[i] += 1
            else :
                res[i] = 1
                mem.append(i)
        
        r = []
        for i in mem : 
            r.append(res[i])
        return list(r)
