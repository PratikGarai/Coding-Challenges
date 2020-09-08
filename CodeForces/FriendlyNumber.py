def main():
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l)
    flag = 0
    for i in range(n-1):
        if(l[i+1]%l[i]):
            flag = 1
            break

    if flag:
        print('NOT FRIENDS')
    else:
        print('FRIENDS')

if __name__=='__main__':
    main()
