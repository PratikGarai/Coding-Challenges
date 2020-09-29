def main():
    n= int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(min_wins(a,b))
    print(max_wins(a,b))

if __name__=='__main__':
    main()
