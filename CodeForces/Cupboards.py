n = int(input())
a = 0
b = 0
for i in range(n):
    c, d = map(int, input().split())
    a += c
    b += d

e = 0
if a<=n//2:
    e += a
else :
    e += n-a
if b<=n//2:
    e += b
else :
    e += n-b
print(e)
