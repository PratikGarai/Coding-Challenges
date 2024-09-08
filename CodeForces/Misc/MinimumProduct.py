def process():
    a,b,x,y,n =  list(map(int, input().split()))

    def get_min(n,a,b,x,y):
        da = min(n, a-x)
        a, n = a-da, n-da
        if n==0:
            return a*b
    
        db = min(n, b-y)
        b = b-db
        return a*b
    
    return min(get_min(n,a,b,x,y), get_min(n,b,a,y,x))

def main():
    for i in range(int(input())):
        print(process())

if __name__=='__main__':
    main()
