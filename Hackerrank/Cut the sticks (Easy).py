n = int(input())
a = list(map(int,input().split()))

a.sort()
l=len(a)
prev=-1
for i in a:
    if (i!=prev):
        print(l)
    prev=i
    l-=1
