def main():
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l)
    mx = l[-1]

    occupied = [0 for i in range(n)]
    
    l_pointer = 0
    h_pointer = l_pointer + 1

    while(h_pointer<n-1 and l_pointer<n-2):

        occupied[l_pointer] = 1

        while(l[h_pointer]<=l[l_pointer] and h_pointer<n-1):
            h_pointer += 1

        print(l[h_pointer],l[l_pointer],l[h_pointer+1], sep=' ', end=' ')
        occupied[h_pointer] = 1
        occupied[h_pointer+1] = 1
        h_pointer += 1

        while(l[l_pointer]!=0 and l_pointer<n-2):
            l_pointer += 1
        if l_pointer>=h_pointer:
            h_pointer = l_pointer+1

    for i in range(n):
        if occupied[i]==0:
            print(l[i], end=' ')
    print()

if __name__=='__main__':
    main()
