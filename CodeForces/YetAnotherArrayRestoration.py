def get_result():
    n, x, y = list(map(int, input().split()))
    
    if n==2:
        return [x,y]

    diff = y-x
    min_d = diff
    for i in range(1, diff):
        if diff%i==0 and diff//i<=n and y-(n-1)*i<=x :
            min_d = i
            break
    arr = []

    c = y
    while(n>0 and c>0):
        arr.append(c)
        n -= 1
        c -= min_d
    
    c = y+min_d
    while(n>0):
        arr.append(c)
        n -= 1
        c += min_d

    return arr

def main():
    t = int(input())
    for i in range(t):
        for j in get_result():
            print(j, end=' ')
        print()

if __name__=='__main__':
    main()
