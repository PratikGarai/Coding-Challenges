class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):

        l = [0 for i in range(B)]
        d = [(0, 0)]

        level = 0
        for i in range(B-1) :
            if A[i]=="I" :
                level += 1
            else :
                level -= 1
            d.append((level, i+1))
        
        d = sorted(d)
        num = 1
        for level, index in d :        
            l[index] = num
            num += 1
        return l
