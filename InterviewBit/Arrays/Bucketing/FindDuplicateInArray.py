class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        s = set({})
        for i in A :
            if i in s :
                return i
            else :
                s.add(i)
        
        return -1
