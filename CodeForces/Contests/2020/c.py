bits=62
mem = [2**i for i in range(bits+1)]

def convert_to_binary_array(a) :
    res = [0 for _ in range(bits)]
    for i in range(bits, -1, -1) :
        if a < mem[i]: 
            continue
        a -= mem[i]
        res[i] = 1
    return res

def solve() :
    b, c, d = map(int, input().split())
    ba = convert_to_binary_array(b)
    ca = convert_to_binary_array(c)
    da = convert_to_binary_array(d)
    aa = convert_to_binary_array(0)

    for i in range(bits+1) :
        if da[i] == 1 :
            if ca[i] == 1 : 
                aa[i] = 0
            else :
                aa[i] = 1
        if da[i] == 0 : 
            if 2**i > d : 
                break
            if 2**i <= b or 2**i <= c :
                print(-1)
                return
    
    a = 0
    for i in range(bits+1) :
        a += 2**i * aa[i]
    
    print(a)

def main() :
    t = int(input())
    for _ in range(t) :
        solve()

if __name__=="__main__" :
    main()