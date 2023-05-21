#User function Template for python3

class Solution:
    def spirallyTraverse(self,matrix, r, c): 
        layer = 0
        res = []
        
        layers = min(r, c)//2
        
        while layer < layers: 
            for i in range(layer, c-1-layer) :
                res.append(matrix[layer][i])
            
            for i in range(layer, r-1-layer):
                res.append(matrix[i][c-1-layer])
            
            for i in range(c-1-layer, layer, -1):
                res.append(matrix[r-1-layer][i])
            
            for i in range(r-1-layer, layer, -1):
                res.append(matrix[i][layer])
            layer += 1
        
        if r<c and r%2==1 : 
            for i in range(layer, c-layer):
                res.append(matrix[r//2][i])
        if c<r and c%2==1:
            for i in range(layer, r-layer):
                res.append(matrix[i][c//2])
        if c==r and c%2==1 and r%2==1 : 
            res.append(matrix[r//2][c//2])
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends
