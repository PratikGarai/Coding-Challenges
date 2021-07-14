n = int(input())
x = 0

for i in range(n):
    l = set([j for j in input()])
    if "+" in l:
        x += 1
    else :
        x -= 1

print(x)
