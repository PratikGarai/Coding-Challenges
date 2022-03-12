class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):

        last = ""
        streak = 0
        st = ""
        for i in A : 
            if i!=last :
                st += last*streak
                last = i
                streak = 1
            else : 
                streak += 1
                if streak==B:
                    last = ""
                    streak = 0
        st += last*streak
        
        return st
