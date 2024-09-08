n, m = map(int, input().split())
s = list(map(int, input().split()))

last = 1
ans = 0


for i in range(m):
    if s[i]>=last :
        ans += s[i]-last
    else :
        ans += n-last+s[i]
    last = s[i]

print(ans)
