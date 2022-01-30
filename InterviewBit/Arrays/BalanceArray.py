class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        l = len(A)
        to = 0
        te = 0
        o = [0 for i in range(l)]
        e = [0 for i in range(l)]

        e[0] = A[0]
        te = A[0]

        for i in range(1, l):
            if i%2==0:
                e[i] = e[i-1]+A[i]
                te += A[i]
                o[i] = o[i-1]
            else :
                o[i] = o[i-1]+A[i]
                to += A[i]
                e[i] = e[i-1]
        
        #print(o, e, to, te)
        count = 0
        
        for i in range(l):
            if i%2!=0:
                if o[i]-A[i]+(te-e[i])==e[i]+(to-o[i]) :
                    count += 1
            else :
                if e[i]-A[i]+(to-o[i])==o[i]+(te-e[i]) :
                    count += 1
        
        return count
