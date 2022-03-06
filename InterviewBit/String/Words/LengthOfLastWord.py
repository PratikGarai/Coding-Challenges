class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):

        if len(A)==0:
            return 0
        words = []
        l = 0
        st = ""
        for i in A :
            if i!=" ":
                st += i
            elif st!="":
                words.append(st)
                st = ""
                l += 1
        if A[-1]!=" ":
            l += 1
            words.append(st)
        if l==0:
            return 0
        return len(words[-1])
