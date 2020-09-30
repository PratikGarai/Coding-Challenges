def min_wins(c,d):

    def compute(arr):
        a = c.copy()
        b = d.copy()

        for i in arr :
            if i==0:
                m = min(a[0], b[2])
                a[0] -= m
                b[2] -= m
            elif i==1:
                m = min(a[1], b[0])
                a[1] -= m
                b[0] -= m
            elif i==2:
                m = min(a[2], b[1])
                a[2] -= m
                b[1] -= m
            elif i==3:
                m = min(a[0], b[0])
                a[0] -= m
                b[0] -= m
            elif i==4:
                m = min(a[1], b[1])
                a[1] -= m
                b[1] -= m
            elif i==5:
                m = min(a[2], b[2])
                a[2] -= m
                b[2] -= m
        return sum(a)

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
