def main():
    a,b = list(map(int, input().split()))
    if (b-a+1)%2 or a>=b:
        print('NO')
    else:
        print('YES')
        for i in range(a, b,2):
            print(i,i+1)

if __name__=='__main__':
    main()
