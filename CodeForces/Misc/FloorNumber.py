def process():
    n, x = list(map(int, input().split()))
    if n<=2:
        print(1)
        return
    else:
        res = (n-2+x)/x
        if(res%1!=0):
            res += 1
        print(int(res))
        return

def main():
    for i in range(int(input())):
        process()

if __name__=='__main__':
    main()
