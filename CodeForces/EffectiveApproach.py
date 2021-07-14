n = int(input())
l1 = list(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))


d = [0 for i in range(100001)]

for i in range(n) :
    d[l1[i]] = i

a = 0
b = 0

for i in range(m):
    a += d[l2[i]]+1
    b += n-d[l2[i]]

print(a,b)
