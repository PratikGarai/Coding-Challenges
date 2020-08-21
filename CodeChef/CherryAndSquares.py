def compute(m , x1, y1, x2, y2 ):
    w = x2-x1+1
    h = y2-y1+1
    if w==1 or h==1:
        return 1
    gmax = 1
    new_m = [[1 for i in range(w)] for j in range(h)]
    for i in range(y1+1,y2+1):
        for j in range(x1+1, x2+1):
            if(max(m[i-1][j-1],m[i-1][j],m[i][j-1])<=m[i][j]):
                new_m[i-y1][j-x1] = min(new_m[i-1][j-1],new_m[i-1][j],new_m[i][j-1])+1
                if(new_m[i-y1][j-x1]>gmax):
                    gmax = new_m[i-y1][j-x1]
    return gmax

def main():
    h,w = list(map(int, input().split()))
    m = [[0 for i in range(w)] for  in range(h)]
    for i in range(h):
        m[h] = list(map(int, input().split()))
    n = int(input())
    results = []
    for i in range(n):
        x1,y1,x2,y2 = list(map(int,input().split()))
        results.append(compute(m,x1-1,y1-1,x2-1,y2-1))
    for i in results :
        print(i)

if __name__ == '__main__':
    main()
