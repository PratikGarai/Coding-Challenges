n = int(input())
if n%2==1 :
    print(-1)
else :
    s = [i for i in range(1, n+1)]
    for i in range(0,n,2):
        s[i], s[i+1] = s[i+1], s[i]
    for i in s:
        print(i, end=" ")
    print()
