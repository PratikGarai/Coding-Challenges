import math 

def get_result():
    x,y,k = list(map(int,input().split()))

    t = (y+1)*k-1+x-2
    trades = t//(x-1) + k

    return int(trades)

def main():
    t = int(input())
    for i in range(t):
        print(get_result())

if __name__=='__main__':
    main()
