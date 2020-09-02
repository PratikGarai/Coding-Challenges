def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = 0
    for i in range(1,n-1):
        if a[i-1]==a[i+1] and a[i-1]==1 and a[i]==0:
            d += 1
            a[i-1], a[i+1] = 0,0
    print(d)

if __name__=='__main__':
    main()
