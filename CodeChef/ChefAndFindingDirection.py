dx = {'L':-1,'R':1,'U':0,'D':0}
dy = {'L':0,'R':0,'U':1,'D':-1}

def compute(a, target,n):
    if target==1:
        return True
    visited = [[0 for i in range(n)] for j in range(n)]
    def traverse(pos , value):
        if value==target-1:
            if pos==[0,0]:
                return True
            else:
                return False
        if visited[pos[0]][pos[1]]==1:
            return False
        visited[pos[0]][pos[1]]=1
        l = []
        for i in a[pos[0]][pos[1]]:
            l.append(traverse((pos[0]+dy[i], pos[1]+dx[i]), value+1))
        if any(l):
            return True
        else :
            return False
    result = traverse([0,0], 0)
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
