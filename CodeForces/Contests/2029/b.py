def solve() :
    n = int(input())
    s1 = input()
    s2 = input()

    s10 = 0
    s11 = 0
    for i in range(n) :
        if s1[i] == '0' :
            s10 += 1
        if s1[i] == '1' :
            s11 += 1

    for i in range(n-1):
        if s10 == 0 or s11 == 0 :
            print("NO")
            return

        if s2[i] == '1' :
            s10 -= 1
        else : 
            s11 -= 1
                
    print("YES")

def main() :
    t = int(input())
    for _ in range(t) :
        solve()

if __name__=="__main__" :
    main()