def get_results():
    n, s = input().split()
    s = int(s)
    su = 0
    ind = -1
    for index,i in enumerate(n):
        su += int(i)
        if(su>=s):
            ind = index
            break
    if ind==-1:
        print(0)
        return
    if su==s and ind==len(n)-1:
        print(0)
        return
    l = ind-1
    l = len(n)-l-1
    print(10**l-int(n[ind:]))

def main():
    t = int(input())
    for i in range(t):
        get_results()

if __name__=='__main__':
    main()
