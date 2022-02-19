class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        A = sorted(A)
        ans = []
        l = len(A)
        ind = 0
        while(A[ind]<0 and ind<l):
            ind += 1
        
        n = ind -1
        p = ind

        while n>=0 and p<l:
            if abs(A[n])>A[p]:
                ans.append(A[p]**2)
                p += 1
            else :
                ans.append(A[n]**2)
                n -= 1
        while n>=0:
            ans.append(A[n]**2)
            n -= 1
        while(p<l):
            ans.append(A[p]**2)
            p += 1

        return ans
