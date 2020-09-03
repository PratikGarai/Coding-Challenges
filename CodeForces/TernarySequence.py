def process(a,b,c,d,e,f):
    s = 0

    if c>e:
        s = 2*e
        c -= e
        e = 0
    else:
        s = 2*c
        c = 0
        e -= c
    if c>f :
        return s
    else :
        c = 0
        f -= c

    if b<=d+e:
        return s
    else :
        s -= 2*f
        return s

def main():
    n = int(input())
    results = []
    for i in range(n):
        f0, f1, f2 = list(map(int, input().split()))
        s0, s1, s2 = list(map(int, input().split()))
        results.append(process(f0, f1, f2, s0, s1, s2))

    for i in results:
        print(i)

if __name__=='__main__':
    main()
