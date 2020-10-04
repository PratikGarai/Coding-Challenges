def process():
    n,m = list(map(int, input().split()))
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    hl = m//2
    vl = n//2

    count = 0
    for i in range(vl):
        for j in range(hl):
            n1,n2,n3,n4 = sorted((a[i][j], a[n-1-i][j], a[i][m-1-j], a[n-1-i][m-1-j]))
            count += min( 3*n4-n1-n2-n3 , n4-n2-n1+n3 , n4+n3-n2-n1 , n4+n3+n2-3*n1)

    if m%2 :
        for i in range(vl):
            count += abs(a[i][hl] - a[n-i-1][hl])
    if n%2:
        for i in range(hl):
            count += abs(a[vl][i] - a[vl][m-1-i])

    print(count)

def main():
    for i in range(int(input())):
        process()

if __name__=='__main__':
    main()
