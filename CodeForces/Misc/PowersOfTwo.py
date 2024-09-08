n, k = map(int, input().split())
b = list(map(int, bin(n)[2:]))
s = sum(b)
if k>n or k<s : 
    print("NO")
else :
    ind = 0
    excess = k - s
    l = len(b)
    for i in range(l-1) :
        if excess >= b[i] :
            b[i+1] += b[i]*2
            excess -= b[i]
            b[i] = 0
        else :
            b[i] -= excess
            b[i+1] += excess*2
            excess = 0
            break

    n = 1
    print("YES")
    for i in range(l) :
        for j in range(b[i]):
            print(2**(l-i-1), end=" ")
