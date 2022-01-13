class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):

        s = sum(B)
        if s%3!=0:
            return 0
        
        s = s//3
        
        a = 0
        b = 0
        acc = 0
        ans = 0

        for i in range(A-1):
            acc += B[i]
            if acc == 2*s :
                b += 1
                ans += a
            if acc == s :
                a += 1
        
        return ans
