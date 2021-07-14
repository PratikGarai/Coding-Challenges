n = int(input())
c = 0
for i in range(n):
    s = sum(list(map(int, input().split())))
    if s>=2 :
        c += 1

print(c)
