m = [[1 for i in range(3)] for j in range(3)]

a = []
for i in range(3):
    a.append(list(map(int, input().split(" "))))

dx = [0,0,-1,0,1]
dy = [0,1,0,-1,0]

for i in range(3):
    for j in range(3):
        x,y = i,j
        if a[i][j]%2==0:
            continue
        for k in range(5):
            nx, ny = x+dx[k], y+dy[k]
            if nx<0 or ny<0 or nx>2 or ny>2 :
                continue
            if m[nx][ny] == 0 : 
                m[nx][ny] = 1 
            else:
                m[nx][ny] = 0

for i in range(3):
    for j in range(3):
        print(m[i][j], end="")
    print()
