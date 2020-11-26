def main():
    a,b = list(map(int, input().split()))
    arr = input().split()
    b = b%a
    arr = arr[b:a] + arr[0:b]
    print(' '.join(arr))
    
if __name__=='__main__':
    main()
