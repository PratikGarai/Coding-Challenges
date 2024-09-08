def process():
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    nz = 1
    atl_0 = 0
    for i in range(n):
        a[i] = a[i]-x
        if a[i]!=0:
            nz = 0
        if a[i]==0:
            atl_0 = 1

    if nz==1:
        print(0)
        return
    
    if sum(a)==0 or atl_0==1:
        print(1)
    else :
        print(2)

def main():
    t = int(input())
    for i in range(t):
        process()

if __name__=='__main__':
    main()
