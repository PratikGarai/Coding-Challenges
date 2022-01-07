
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):

        l = len(A)
        ans = [0 for i in range(l)]
        carry = 1
        s = 0

        for i in range(l-1, -1, -1):
            s = carry + A[i]
            carry = s//10
            ans[i] = s%10

        if carry==1 :
            return [1]+ans
        
        i = 0
        while(ans[i]==0):
            i += 1
            if i==l :
                break
        
        return ans[i:]
