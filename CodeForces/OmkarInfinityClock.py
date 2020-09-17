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

    return l

def main():
    t = int(input())
    for i in range(t):
        for i in get_result():
            print(i,end=' ')
        print()

if __name__=='__main__':
    main()
