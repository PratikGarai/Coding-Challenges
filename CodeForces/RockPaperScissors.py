def min_wins(a,b):
    l1 = min(a[0],b[2])
    l2 = min(a[1],b[0])
    l3 = min(a[2],b[1])

    a[0] -= l1
    b[2] -= l1
    a[1] -= l2
    b[0] -= l2
    a[2] -= l3
    b[1] -= l3

    d1 = min(a[0],b[0])
    d2 = min(a[1],b[1])
    d3 = min(a[2],b[2])

    a[0] -= d1
    b[0] -= d1
    a[1] -= d2
    b[1] -= d2
    a[2] -= d3
    b[2] -= d3

    print(a)
    print(b)
    
    return sum(a)

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
