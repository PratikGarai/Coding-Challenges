def get_result():
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))

    return l

def main():
    t = int(input())
    for i in range(t):
        for i in get_result():
            print(i,end=' ')
        print()

if __name__=='__main__':
    main()
