import math

def solve() :
    n, k = map(int, input().split())
    if k == 1 :
        print(n)
        return
    ops = 0
    while n != 0 : 
        if n < k : 
            ops += n
            break
        p = int(math.log(n, k))
        if p==1 :
            ops += n//k
            n = n%k
        else :
            n -= k**p
            ops += 1
    print(ops) 

def main() :
    t = int(input())
    for _ in range(t) :
        solve()

if __name__=="__main__" :
    main()