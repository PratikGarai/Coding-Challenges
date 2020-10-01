
n=int(input())
a=list(map(int,input().split()))
print(n-max([a.count(i) for i in a]))
