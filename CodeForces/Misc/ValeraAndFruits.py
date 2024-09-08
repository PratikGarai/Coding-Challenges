n, v = map(int, input().split())
d = {}
for i in range(n):
    a,b = map(int, input().split())
    if a in d :
        d[a] += b
    else :
        d[a] = b

mi = min(d.keys())
ma = max(d.keys())

c = 0
for i in range(mi, ma+3):
    quota = v
    if i-1 in d :
        if quota>d[i-1]:
            c += d[i-1]
            quota -= d[i-1]
            d[i-1] = 0
        else :
            c += quota
            d[i-1] -= quota
            quota = 0
    if i in d :
        if quota>d[i]:
            c += d[i]
            quota -= d[i]
            d[i] = 0
        else :
            c += quota
            d[i] -= quota
            quota = 0
print(c)
