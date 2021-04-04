a = input()
b = input()

la = len(a)
lb = len(b)

mat = [[0 for i in range(la+1)] for j in range(lb+1)]

for i in range(1, la+1):
    for j in range(1, lb+1):
        if a[i-1]==b[j-1]:
            mat[i][j] = 1+mat[i-1][j-1]
        
        if mat[i-1][j]>mat[i][j]:
            mat[i][j] = mat[i-1][j]
        if mat[i][j-1]>mat[i][j]:
            mat[i][j] = mat[i][j-1]

print(mat[la][lb])
