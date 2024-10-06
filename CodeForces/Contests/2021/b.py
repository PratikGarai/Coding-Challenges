def solve() :
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    d = {}
    for i in a :
        if i in d :
            d[i] += 1
        else :
            d[i] = 1
    mex = 0
    while mex < n:
        if mex not in d :
            if mex-x in d and d[mex-x] > 1 : 
                d[mex-x] -= 1
                d[mex] = 1
            else :
                break
        else :
            if d[mex] > 1 : 
                if mex+x in d :
                    d[mex+x] += d[mex] - 1
                else :
                    d[mex+x] = d[mex]-1
        mex += 1
    print(mex)
                

def main() :
    t = int(input())
    for _ in range(t) :
        solve()

if __name__=="__main__" :
    main()