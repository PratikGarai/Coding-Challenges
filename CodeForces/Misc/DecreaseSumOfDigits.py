def get_sum(n):
    s = 0
    while(n):
        s += n%10
        n = n//10
    return int(s)

def get_results():
    n, s = list(map(int, input().split()))
    
    presum = get_sum(n)
    if presum<=s:
        return 0
    
    mul = 1
    moves = 0 
    while(presum>s):
        d = (n//mul)%10
        if(d!=0):
            dif = (10-d)*mul
            n += dif
            moves += dif
        presum = get_sum(n)
        mul = mul*10
    return moves

def main():
    t = int(input())
    res = []
    for i in range(t):
        res.append(get_results())

    for i in res :
        print(i)

if __name__=='__main__':
    main()
