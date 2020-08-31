dx = {'L':-1,'R':1,'U':0,'D':0}
dy = {'L':0,'R':0,'U':-1,'D':1}

def compute(a, target,n):
    if target==1:
        return True
    visited = [[0 for i in range(n)] for j in range(n)]
    def traverse(y,x,value):
        # print(y,x)
        if value==target:
            if x==0 and y==0:
                return True
            else:
                return False
        if visited[y][x]==1:
            return False
        visited[y][x] = 1
        l = []
        for i in a[y][x]:
            l.append(traverse(y+dy[i], x+dx[i], value+1))
        visited[y][x] = 0
        if any(l):
            return True
        else :
            return False
    result = traverse(0,0, 0)
    print(result)

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
