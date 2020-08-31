dx = {'L':-1,'R':1,'U':0,'D':0}
dy = {'L':0,'R':0,'U':1,'D':-1}

def compute(a, target,n):
    if target==1:
        return True
    visited = [0 for i in range(target)]
    v = [([0,0],0)]
    max_val = 0
    while v!=[]:
        lv = v.pop()
        val = lv[1]
        if val>max_val:
            max_val = val
        p = lv[0]
        visited[p[0]*n+p[1]]=1
        for i in a[p[0]][p[1]]:
            if visited[(p[0]+dy[i])*n+(p[1]+dx[i])]==0:
                v.append(([p[0]+dy[i], p[1]+dx[i]],val+1))
    print(max_val)
    if max_val==target:
        return True

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
