a = []
for i in range(5):
    a.append(list(map(int, input().split())))

x,y = 0,0
for i in range(5):
    for j in range(5):
        if a[i][j]==1:
            x,y = i,j

print(abs(x-2)+abs(y-2))
