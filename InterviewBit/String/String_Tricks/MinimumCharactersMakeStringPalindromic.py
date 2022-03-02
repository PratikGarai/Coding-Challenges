class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        l = len(A)
        for end in range(l-1, -1, -1) :
            isPalin = True
            if end%2!=0 : 
                rng = (end+1)//2
            else :
                rng = end//2
            for i in range(rng) :
                if A[i]!=A[end-i]:
                    isPalin = False
                    break
            if isPalin : 
                break
        
        return l-end-1
