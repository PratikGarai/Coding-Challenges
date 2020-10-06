def process():
    n = int(input())
    coins = 0
    while(n>0):
        if n%2==1:
            coins += 1
            n = (n-1)>>1
        else :
            n = n>>1
            coins += n
            n -= 1
    print(coins)

def main():
    for i in range(int(input())):
        process()

if __name__=='__main__':
    main()
