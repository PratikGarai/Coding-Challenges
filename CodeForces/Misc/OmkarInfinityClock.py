def get_result():
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))

    if k==0 :
        return k
    mx = max(l)
    for i in range(n):
        l[i] = mx-l[i]
    
    if k%2==1:
        return l
    mx = max(l)
    for i in range(n):
        l[i] = mx-l[i] 

    return l

def main():
    t = int(input())
    for i in range(t):
        for i in get_result():
            print(i,end=' ')
        print()

if __name__=='__main__':
    main()
