t = int(input())

for i in range(t) :

    n = int(input())
    w = list(map(int, input().split()))
    s = sum(w)

    if n%s==0 : 
        res = ((n//s)-1)*7
        n = s
    else :
        res = (n//s)*7
        n = n%s

    steps = 7
    for i in range(7) :
        ind = i
        count = 0
        target = n

        while(count!= 7) :
            count += 1
            ind += 1
            if(ind==7) :
                ind = 0
            target -= w[ind]
            if(target==0) :
                break

        steps = min(steps, count)

    res += steps
    print(res)
