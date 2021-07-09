n = int(input())
s = list(map(int, input().split()))

mi = s[0]
mii = 0
ma = s[0]
mai = 0

for i in range(1, n):
    if s[i]<=mi :
        mi = s[i]
        mii = i
    if s[i]>ma:
        ma = s[i]
        mai = i

d = mai + n - mii -1
if mai>mii:
    d -= 1
print(d)
