def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = []
        for i in range(n):
            a.append(input().split())
        compute(a)

if __name__=='__main__':
    main()
