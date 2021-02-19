def isPrime(n):
    if n<=3 :
        return True
    
    for i in range(2, n):
        if n%i==0:
            return False
    return True

a,b = map(int, input().split())
flag = True

if not isPrime(a) or not isPrime(b):
    flag = False
    print("NO")
else :
    for i in range(a+1,b):
        if isPrime(i):
            flag = False
            print("NO")
            break
if flag:
    print("YES")
