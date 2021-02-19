l = int(input())
s = [i for i in input()]
c = 0

last = s[0]
for i in range(1, l):
    if s[i]==last :
        c += 1
    else :
        last = s[i]

print(c)
