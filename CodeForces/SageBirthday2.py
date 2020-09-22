def main():
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l)
    mx = l[-1]

    p = [0 for i in range(n)]
    
    l_pointer = 0
    h_pointer1 = l_pointer + 1
    h_pointer2 = l_pointer + 2
    
    while(l[l_pointer] != mx or l_pointer<n-2):
        
        #loop to find h_pointer1
        while(l[h_pointer1]<=l[l_pointer] and l[h_pointer1]==1):
            h_pointer1 += 1
            if h_pointer1==n-1:
                break
        if h_pointer1==n-1:
            break
        p[h_pointer1] = 1

        h_pointer2 = h_pointer1+1 
        #loop to find h_pointer2
        while(l[h_pointer2]<=l[l_pointer]):
            h_pointer2 += 1
            if h_pointer2==n:
                break
        if h_pointer2==n:
            break
        p[h_pointer2] = 1
        
        print(l[h_pointer1],l[l_pointer],l[h_pointer2],sep=' ', end=' ')

        l_pointer += 1
        #loop to find new l_pointer
        while(p[l_pointer]==1):
            l_pointer += 1
            if l_pointer==n-2:
                break
        if l_pointer==n-2:
            break

    for i in range(n):
        if p[i]!=1:
            print(l[i], end=' ')

    print()

if __name__=='__main__':
    main()
