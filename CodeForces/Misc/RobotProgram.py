def process():
    a,b = list(map(int, input().split()))
    s = 0

    m = min(a,b)
    s = m*2
    a -= m
    b -= m

    if a==0 and b==0 :
        return s
    a = a if b==0 else b
    if b==1 :
        s += 1
    else :
        s += 2*a -1 
    return s


def main():
    for i in range(int(input())):
        print(process())

if __name__=='__main__':
    main()
