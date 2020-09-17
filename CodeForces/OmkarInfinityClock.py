def get_result():
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))

    mig = min(l)
    mil = mig
    while(mig!=0 and k>0):
        for i in range(n):
            l[i] -= mil
            if l[i]<mig:
                mig = l[i]
        k-=1
        mil = mig
    return l

def main():
    t = int(input())
    for i in range(t):
        print(get_result())

if __name__=='__main__':
    main()
