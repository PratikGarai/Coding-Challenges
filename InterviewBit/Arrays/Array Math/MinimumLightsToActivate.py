class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        le = len(A)
        l = 0
        ans = 0

        while(l<le) :
            ind = l
            f = False
            for i in range(l, min(l+B, le)) :
                if A[i]==1:
                    f = True
                    ind = i
            
            if not f :
                f = False
                for i in range(l, max(0, l-B), -1) :
                    if A[i]==1:
                        f = True
                        ind = i
                        break
                
                if not f : 
                    return -1
            
            l = ind + B
            ans += 1
        
        return ans
