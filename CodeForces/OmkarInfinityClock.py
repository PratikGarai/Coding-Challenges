def get_result():
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))

    if k==0 :
        return k
    mx = max(l)
    mi = min(l)
    for i in range(n):
        l[i] = mx-l[i]
    #all negatives turn to positive
    if k==1:
        return l

    mx = max(l)
    for i in range(n):
        l[i] = mx-l[i]
    #the first 0 appears
    if k==2:
        return l

    mx =  max(l)
    if mi<0:
        k -= 1
    if k%2==1:
        for i in range(n):
            if l[i]==0:
                l[i] = mx
            elif l[i]==mx:
                l[i] = 0
            else:
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
