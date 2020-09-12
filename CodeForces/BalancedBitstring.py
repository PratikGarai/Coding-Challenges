def checker(a, n , k):
        #getting initial window stats
        deficiency = -1
        n0, n1, qm = 0, 0, 0
        flag = 1
        for i in range(k):
            if a[i]=='0':
                n0 += 1
            elif a[i]=='1':
                n1 += 1
            else :
                qm += 1
        if n1!=n0 and qm!=abs(n1-n0) :
            return 0
        if n1<n0:
            deficiency = 1
        elif n0<n1:
            deficiency = 0


def main():
    t = int(input())
    for i in range(t):
        n, k = list(map(int, input().split()))
        a = input()
        flag = checker(a,n,k)
        if flag==1:
            print("YES")
        else:
            print("NO")

if __name__=='__main__':
    main()
