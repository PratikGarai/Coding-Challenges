
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        md = 10**9 + 7
        ans = 0
        l = len(A)
        vowels = {"a", "e", "i", "o", "u"}

        v = 0
        c = 0

        for i in range(l-1, -1, -1):
            if A[i] in vowels : 
                v += 1
                ans += c
                ans = ans%md
            else :
                c += 1
                ans += v
                ans = ans%md
        
        return ans
