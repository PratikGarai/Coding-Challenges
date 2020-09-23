def main():
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l)
    mx = l[-1]

    occupied = [0 for i in range(n)]
    
    low = 0
    high = 1
    num = 0

    while(l[high]==l[low] and high<n):
        high += 1

    occupied[low] = 1
    occupied[high] = 1

    while(low<n-1 and high<n):


    for i in range(n):
        if occupied[i]==0:
            print(l[i], end=' ')
    print()

if __name__=='__main__':
    main()
