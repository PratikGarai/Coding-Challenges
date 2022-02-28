class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        s = ""
        for i in A : 
            if i.isupper():
                s += i.lower()
            elif i.islower() :
                s += i.upper()

        return s
