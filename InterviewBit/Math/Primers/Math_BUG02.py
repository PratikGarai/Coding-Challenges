
class Solution:
	# @param A : integer
	# @return a list of list of integers
	def squareSum(self, A):
		ans = []
		a = 0
		while a * a < A:
			b = a
			while b * b < A:
				if a * a + b * b == A:
					newEntry = [a, b]
					ans.append(newEntry)
				b += 1
			a += 1
		return ans
