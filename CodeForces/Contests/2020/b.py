mx = 10**18

def solve() :
    k = int(input())

    p = int(k**0.5)
    while True :
        nv = (p+1)**2 - (p+1) 
        if nv < k :
            p += 1
        else : 
            print(p**2 + (k - (p**2 - p)))
            break

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__=="__main__":
    main()