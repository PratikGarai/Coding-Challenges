class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        s = 0
        m = 1
        base = ord("A")
        for i in A[::-1] :
            s += ((ord(i)-base+1)*m)
            m = m*26
        
        return s
