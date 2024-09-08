def process(a,b,c,d,e,f):
    s = 0
    m2 = min(c,e)
    s += 2*m2
    c -= m2
    e -= m2
    f -= c
    f -= a
    if f>0:
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
