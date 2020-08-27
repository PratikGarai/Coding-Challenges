def get_mid(a,b):
    return 0

def compute(n,l):
    le = len(l)
    lst = []
    for i in range(0, le-1):
        lst.append(l[i])
        n = int(n/l[i])
        g = get_mid(l[i],l[i+1]))
        n = int(n/g)
        lst.append(g)
    return lst

def  main():
    n = int(input())
    l = list(map(int, input.split()))
    print(compute(n,l))

if __name__=='__main__':
    main()
