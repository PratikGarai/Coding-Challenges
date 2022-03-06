class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        md = 10**9 + 7
        B = sorted(B)
        l = len(B) 

        def factorial(n) :
            prod = 1
            for i in range(1, n+1):
                prod = prod * i
            return prod
        
        def mul(a, b):
            return ((a%md)*(b%md))%md
        
        ways = factorial(A-l)

        ways = ways//factorial(B[0]-1)
        ways = ways//factorial(A-B[-1])

        gaps = []

        for i in range(1, l):
            if B[i]-B[i-1]>1:
                gaps.append(B[i]-B[i-1]-1)
        
        for i in gaps:
            ways = ways//factorial(i)
        
        for i in gaps:
            ways = mul(ways, 2**(i-1))

        return ways
