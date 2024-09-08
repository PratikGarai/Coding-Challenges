def process():
    n,k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    if(k>n-1):
       k = n-1
    arr = sorted(arr, reverse = True)
    
    print(sum(arr[0:k+1]))


def main():
    for i in range(int(input())):
        process()

if __name__=='__main__':
    main()
