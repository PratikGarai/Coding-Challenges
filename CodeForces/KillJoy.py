def process():
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    nz = 1
    for i in range(n):
        a[i] = a[i]-x
        if a[i]!=0:
            nz = 0

    if nz==1:
        print(0)
        return
    
    if sum(a)==0:
        print(1)
    else :
        print(2)

def main():
    t = int(input())
    for i in range(t):
        process()

if __name__=='__main__':
    main()
