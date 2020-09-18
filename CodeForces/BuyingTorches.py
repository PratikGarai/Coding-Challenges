def get_result():
    x,y,k = list(map(int,input().split()))

    s = (y+(k*y))/(x-1)
    if(s%1!=0):
        s+=1
    s = int(s)
    s+=k
    return s

def main():
    t = int(input())
    for i in range(t):
        print(get_result())

if __name__=='__main__':
    main()
