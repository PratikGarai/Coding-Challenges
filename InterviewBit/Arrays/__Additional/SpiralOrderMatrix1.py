class Solution:
	# @param A : tuple of list of integers
	# @return a list of integers
	def spiralOrder(self, A):

        l = len(A)

        if l==0:
            return []

        ans = []
        b = len(A[0])

        mi = min(l, b)

        for layer in range(mi//2) :
            for j in range(layer, b-layer-1):
                ans.append(A[layer][j])
            for j in range(layer, l-layer-1):
                ans.append(A[j][b-layer-1])
            for j in range(layer, b-layer-1):
                ans.append(A[l-layer-1][b-j-1])
            for j in range(layer, l-layer-1):
                ans.append(A[l-j-1][layer])

        if mi%2==0:
            return ans
        
        if l<b :
            ind = l//2
            for i in range(mi//2, b-mi//2):
                ans.append(A[ind][i])
        else :
            ind = b//2
            for i in range(mi//2, l-mi//2):
                ans.append(A[i][ind])
        return ans
