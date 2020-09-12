def checker(a, n , k):
        #getting initial window stats
        n0, n1, qm = 0, 0, 0
        for i in range(k):
            if a[i]=='0':
                n0 += 1
            elif a[i]=='1':
                n1 += 1
            else :
                qm += 1
        if n0!=n1 and qm<abs(n1-n0):
            return 0
        for i in range(1, n-k+1):
            if a[i-1]=='1' and a[i+k-1]=='0':
                return 0
            elif a[i-1]=='0' and a[i+k-1]=='1':
                return 0
            elif a[i-1]=='0' and a[i+k-1]=='?':
                a[i+k-1] = '0'
            elif a[i-1]=='1' and a[i+k-1]=='?':
                a[i+k-1] = '1'
        n0, n1, qm = 0, 0, 0
        for i in range(n-k,n):
            if a[i]=='0':
                n0 += 1
            elif a[i]=='1':
                n1 += 1
            else :
                qm += 1
        if n0!=n1 and qm<abs(n1-n0):
            return 0
        return 1

def main():
    t = int(input())
    res = []
    for i in range(t):
        n, k = list(map(int, input().split()))
        a = [i for  i in input()]
        flag = checker(a,n,k)
        if flag==1:
            print("YES")
        else:
            print("NO")
    for i in res:
        print(i)

if __name__=='__main__':
    main()
