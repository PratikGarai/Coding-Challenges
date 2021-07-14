import math

n,m = map(int, input().split())
s = list(map(int, input().split()))


mx = 0
ind = 0
for i in range(n):
    if math.ceil(s[i]/m)>=mx:
        mx = math.ceil(s[i]/m)
        ind = i

print(ind + 1)
