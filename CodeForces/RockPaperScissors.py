def min_wins(a,b):
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
