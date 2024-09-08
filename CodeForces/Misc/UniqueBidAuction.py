def process():
    n = int(input())
    le = list(map(int, input().split()))

    if n==1 :
        return 1

    l = sorted(le)
    repeated = False
    last = l[0]

    num = -1
    for i in l[1:] :
        if i==last:
            repeated = True
        elif not repeated :
            num = last
            break
        else :
            repeated = False
            last = i
    if not repeated:
        num = last
    
    if num==-1:
        return -1

    for i in range(n):
        if le[i]==num:
            return i+1


def main():
    for i in range(int(input())):
        print(process())

if __name__=='__main__':
    main()
