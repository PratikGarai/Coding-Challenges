def main():
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l)
    mx = m[-1]

    p = [0 for i in range(n)]
    
    l_pointer = 0
    h_pointer1 = l_pointer + 1
    h_pointer2 = l_pointer + 2
    
    while(l[l_pointer] != mx or l_pointer<n-2):
        h_pointer1 = l_pointer + 1
        h_pointer2 = l_pointer + 2
        
        #loop to find h_pointer1

        #loop to find h_pointer2

        #loop to find new l_pointer

if __name__=='__main__':
    main()
