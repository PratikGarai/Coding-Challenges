def main():
    l,mn,ma = list(map(int, input().split()))
    if mn>l :
        mn = l
    if ma>l :
        ma = l

    mn_sum = l-mn+1 
    c = 1
    for i in range(mn-1):
        c *= 2
        mn_sum += c

    c = 1
    mx_sum = 1
    for i in range(1,ma):
        c *= 2
        mx_sum += c
    mx_sum += (l-ma)*c

    print(mn_sum,mx_sum)

if __name__=='__main__':
    main()
