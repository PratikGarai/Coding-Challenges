def main():
    n  = int(input())
    l = list(map(int, input().split()))
    l  = sorted(l)

    ind = n//2
    while(l[ind]==l[ind-1] and ind>1):
        ind -= 1

    b1 = l[:ind]
    b2 = l[ind:]

    l1 = ind
    l2 = n-ind

    if l1<l2:
        print(l1)
    else:
        print(l1-1)

    i1 = 0
    i2 = 0
    for i in range(2*l1):
        if i%2==1:
            print(b1[i1], end=' ')
            i1 += 1
        else :
            print(b2[i2], end=' ')
            i2 += 1

    while(i2<l2):
        print(b2[i2], end = ' ')
        i2 += 1

    print()

if __name__=='__main__':
    main()
