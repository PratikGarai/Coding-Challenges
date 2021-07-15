n = int(input())
d = {}
for i in range(n):
    t = input()
    if t not in d :
        d[t] = 1
    else :
        d[t] += 1

print(sorted(d.items(), key = lambda x : x[1], reverse = True)[0][0])
