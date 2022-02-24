class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        A = set(A)
        z = 0 in A 
        l2 = len(str(C))
        l = len(A)

        if l==0 :
            return 0
        
        if B==1 :
            ans = 0
            for i in A :
                if i<C :
                    ans += 1
            return ans

        if B<l2 :
            if z : 
                return (l-1)*(l**(B-1))
            else : 
                return l**B
        elif B==l2 :
            arr = [int(i) for i in str(C)]
            dp = [0 for i in range(B)]

            for i in range(B) :
                for j in A : 
                    if j<arr[i] : 
                        dp[i] += 1
            
            if z : 
                dp[0] -= 1
            ans = 0
            mul = 1
            def recur(index):
                if index==B : 
                    return 0
                less = (dp[index])*(l**(B-index-1))
                equal = 0
                if arr[index] in A : 
                    equal = recur(index+1)
                return equal+less
            return recur(0)
        else :
            return 0
