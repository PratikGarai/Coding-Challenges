def main():
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l)
    mx = l[-1]

    occupied = [0 for i in range(n)]
    
    for i in range(n):
        if occupied[i]==0:
            print(l[i], end=' ')
    print()

if __name__=='__main__':
    main()
