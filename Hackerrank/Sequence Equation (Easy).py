n=int(input())
p=list(map(int,input().split()))

for x in range(n):
    z=p.index(x+1)+1
    print(p.index(z)+1)
