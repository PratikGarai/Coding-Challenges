n = int(input())
s = sum(list(map(int, input().split())))
c = 0
for i in range(1, 6):
    if (s+i)%(n+1)!=1:
        c += 1

print(c)
