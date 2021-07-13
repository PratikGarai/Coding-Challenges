a,b,c = map(int, input().split())
s = set([a,b,c])
d = False
for i in range(1,10001):
    for j in range(1, 10001):
        if i*j>10000:
            break
        if i*j not in s:
            continue
        for k in range(1, 10001):
            if i*k>10000 or j*k>10000:
                break
            if i*j==a and j*k==b and i*k==c:
                print(4*(i+j+k))
                d = True
                break
        if d : 
            break
    if d : 
        break
