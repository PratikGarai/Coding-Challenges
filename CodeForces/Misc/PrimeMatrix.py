n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

mx = 100003
arr = [True for i in range(mx+1)]
arr[0] = False
arr[1] = False
arr[2] = True

def generatePrimes(mx):
    for i in range(2, mx+1):
        if not arr[i]:
            continue
        else :
            j = i
            while(j+i<mx):
                j += i
                arr[j] = False
generatePrimes(mx)

def nextPrime(n):
    i = n
    while(not arr[i]):
        i += 1
    return i-n

for i in range(n):
    for j in range(m):
        a[i][j] = nextPrime(a[i][j])

mi = 5000000
for i in range(n):
    for j in range(m):
        s = sum(a[i])
        mi = min(s,mi)
    
for j in range(m):
    s = 0
    for k in range(n):
        s += a[k][j]
    mi = min(s,mi)
print(mi)
