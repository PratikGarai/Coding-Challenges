def process():
    n,k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    if(k>n-1):
       k = n-1
    l_sum = sum(arr[0:k+1])
    g_sum = l_sum
    l_ind, h_ind = 0, k+1
    
    while(h_ind<n):
        l_sum += arr[h_ind]-arr[l_ind]
        if(l_sum>g_sum):
            g_sum = l_sum
        l_ind += 1
        h_ind += 1

    print(g_sum)


def main():
    for i in range(int(input())):
        process()

if __name__=='__main__':
    main()
