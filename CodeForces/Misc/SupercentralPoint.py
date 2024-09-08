def n_type(x,y,nx,ny):
    if nx>x and ny==y:
        return 0
    if nx<x and ny==y:
        return 1
    if nx==x and ny>y:
        return 2
    if nx==x and ny<y:
        return 3
    return -1


n = int(input())
a = [[0,0,0,0] for i in range(n)]
b = []

for i in range(n):
    x,y = map(int, input().split())
    b.append((x,y))

for i in range(n):
    for j in range(n):
        d = n_type(*b[i], *b[j])
        if d!=-1:
            a[i][d] = 1

c = 0
for i in range(n):
    if sum(a[i])==4:
        c += 1
print(c)
