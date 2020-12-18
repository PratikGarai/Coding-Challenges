k = int(input())
for z in range(k):
    l = int(input())
    n  = list(map(int,input().split()))
    c = 0
    for i in range(l-1):
        for j in range(i+1,l):
            if n[i]>n[j]:
                c += 1
    if c%2==0:
        print('YES')
    else:
        print('NO')
