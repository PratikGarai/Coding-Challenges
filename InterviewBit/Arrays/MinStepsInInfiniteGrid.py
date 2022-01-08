class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
	def coverPoints(self, A, B):
        l = len(A)

        if l==0:
            return 0

        steps = 0
        a = A[0]
        b = B[0]
        for i in range(1, l) :
            diffA = abs(A[i]-a)
            diffB = abs(B[i]-b)
            steps += max(diffA, diffB)
            a = A[i]
            b = B[i]
        
        return steps
