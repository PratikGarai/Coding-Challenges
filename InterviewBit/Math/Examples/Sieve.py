class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):

        if A<=1 :
            return []

        arr = [False for i in range(A)]
        for i in range(2, A):
            if arr[i]:
                continue
            fac = 2*i
            while fac<A :
                arr[fac] = True
                fac += i
        
        ans = []
        for i in range(2, A):
            if not arr[i]:
                ans.append(i)
        
        return ans
