def gcd_arr(arr):
    
    def gcd(a, b):
        if(a==0):
            return b
        return(b%a, a)
    g = arr[0]
    for i in arr[1:]:
        g = gcd(g, i)
    return g

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    mn = min(arr)
    gcd = gcd_arr(arr)
    k = factorize(gcd)
    print(k)

if __name__=='__main__':
    main()
