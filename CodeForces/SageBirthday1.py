def main():
    n  = int(input())
    l = list(map(int, input().split()))
    l  = sorted(l)
    b1 = l[:n//2]
    b2 = l[n//2:]

    if n%2==0:
        print(n//2 -1)
    else:
        print(n//2)

    i1 = 0
    i2 = 0
    for i in range(n):
        if i%2==1:
            print(b1[i1], end=' ')
            i1 += 1
        else :
            print(b2[i2], end=' ')
            i2 += 1

if __name__=='__main__':
    main()
