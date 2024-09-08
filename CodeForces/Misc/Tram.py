n = int(input())
m = 0
c = 0
for i in range(n):
    a,b = map(int, input().split())
    c = c-a+b
    m = max(m, c)

print(m)
