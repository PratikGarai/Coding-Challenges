n = int(input())
s = list(map(int, input().split()))

md = abs(s[0]-s[-1])
i1 = n-1
i2 = 0
for i in range(n-1):
    if abs(s[i]-s[i+1])<md :
        md = abs(s[i]-s[i+1])
        i1, i2 = i, i+1

print(i1+1, i2+1)
