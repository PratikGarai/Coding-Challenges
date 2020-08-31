dx = {'L':-1,'R':1,'U':0,'D':0}
dy = {'L':0,'R':0,'U':-1,'D':1}

def compute(a, target,n):
    if target==1:
        return True
    visited = [[0 for i in range(n)] for j in range(n)]
    def traverse(y,x,value):
        if value==target:
            if x==0 and y==0:
                return True
            else:
                return False
        if visited[y][x]==1:
            return False
        visited[y][x] = 1
        for i in a[y][x]:
            res = traverse(y+dy[i], x+dx[i], value+1)
            if res:
                a[y][x] = i
                return True
        visited[y][x] = 0
        return False
    result = traverse(0,0, 0)
    if result :
        print('YES')
        for i in range(n):
            print(' '.join(a[i]))
    else:
        print('NO')

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = []
        for i in range(n):
            a.append(input().split())
        compute(a, n**2,n)

if __name__=='__main__':
    main()
