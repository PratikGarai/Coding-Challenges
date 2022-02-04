class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        vowels = {"a", "e", "i", "o", "u"}
        A = A.lower()
        md = 10003
        l = len(A)
        ans = 0
        for i in range(l):
            if A[i] in vowels : 
                ans += l-i
                ans = ans%md
        
        return ans
