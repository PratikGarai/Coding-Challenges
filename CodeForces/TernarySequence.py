def process(a,b,c,d,e,f):
    s = 0

    #handling 2 using 1
    if c>e:
        s = 2*e
        c -= e
        e = 0
    else:
        s = 2*c
        c = 0
        e -= c
    #handling 2 using 2
    if c>f :
        return s
    else :
        c = 0
        f -= c

   #handling 1
   if b<=d+e :
       return s
   else :
       s -= 2*f
       return s

def main():
    n = input()
    results = []
    for i in range(n):
        f0, f1, f2 = list(map(int, input().split()))
        s0, s1, s2 = list(map(int, input().split()))
        results.append(process(f0, f1, f2, s1, s2, s3))

    for i in results:
        print(i)

if __name__=='__main__':
    main()
