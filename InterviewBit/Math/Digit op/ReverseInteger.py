class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        neg = A<0
        if neg : 
            A = A*-1
        buf = 0
        while A!=0 : 
            buf = buf*10 + A%10
            A = A//10
        if buf>=(2**31)-1 :
            return 0
        if neg : 
            buf = buf*-1
        return buf
