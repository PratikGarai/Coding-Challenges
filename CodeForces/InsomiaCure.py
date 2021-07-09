k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

dr = [0 for i in range(d)]

for i in range(k-1,d,k):
    dr[i] = 1
for i in range(l-1,d,l):
    dr[i] = 1
for i in range(m-1,d,m):
    dr[i] = 1
for i in range(n-1,d,n):
    dr[i] = 1

print(sum(dr))
