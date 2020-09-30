def min_wins(c,d):
    a = c.copy()
    b = d.copy()

    min_wins = sum(a)
    def compute(arr):
        for i in arr :
            elif i==0:
                pass
            elif i==1:
                pass
            elif i==2:
                pass
            elif i==3:
                pass
            elif i==4:
                pass
            elif i==5:
                pass

        return 0

    def check_permute(ind, arr):
        if ind==5:
            return compute(arr)
        m = 10000000000
        for i in range(ind, 6):
            m = min(m, check_permute(ind+1,arr[:ind]+arr[i:i+1]+arr[ind:i]+arr[i+1:6]))
        return m
    c = check_permute(0, [0,1,2,3,4,5])
    return c

def max_wins(a, b):
    return( min(a[0],b[1])+min(a[1],b[2])+min(a[2],b[0]))

def main():
    n= int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(min_wins(a.copy(),b.copy()), end = ' ')
    print(max_wins(a,b))

if __name__=='__main__':
    main()
