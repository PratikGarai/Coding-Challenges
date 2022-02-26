class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):

        A = A.lower()
        s = ""
        for i in A : 
            if i.isalpha() or i.isdigit():
                s += i

        return 1 if s==s[::-1] else 0
