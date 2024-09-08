n = int(input())
s = list(map(int, input().split()))

ma = s[0]
mi = s[0]
c = 0
for i in range(1, n):
    if s[i]>ma :
        ma = s[i]
        c += 1
    if s[i]<mi :
        mi = s[i]
        c += 1

print(c)
