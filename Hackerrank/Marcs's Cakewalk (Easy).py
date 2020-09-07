from math import pow
n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
s=0
for i in range(n):
    s+=pow(2,i)*a[i]
print(int(s))
