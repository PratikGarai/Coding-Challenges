class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        if A<0 :
            return 0
        dig = 1
        while 10**dig<A :
            dig += 1
        if dig <= 1 :
            return 1
        p = dig
        for i in range(dig//2) :
            if A%10 != A//(10**(p-1)) : 
                return 0
            A = A%(10**(p-1))
            A = A//10
            p -= 2
        return 1
