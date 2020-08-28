n=int(input())
a=list(map(int,input().split()))
m=1000
f=0
for i in range(n):
    if a.count(a[i])>1:
        if a[i] in a[i+1:]:
            j=a.index(a[i],i+1)
            m=min(m,j-i)
            f=1

if f:
    print(m)
else:
    print(-1)
