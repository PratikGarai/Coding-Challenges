def min_counter(a,n):
    a.append(a[n-1]+2)
    sum_of_mins = 0
    segment_min = n
    digit_count = 1
    for i in range(1,n+1):
        if a[i]-a[i-1]>=1:
            if digit_count<segment_min:
                segment_min = digit_count
            digit_count = 1
            if a[i]-a[i-1]>1:
                sum_of_mins += segment_min
                segment_min = n
        else :
            digit_count += 1
    return sum_of_mins

def main():
    n = int(input())
    a = list(map(int, input().split()))
    t = int(input())
    results = []
    for i in range(t):
        s = list(map(int, input().split()))
        if s==[2]:
            result = min_counter(sorted(a), n)
            results.append(result)
        else :
            a[s[1]-1] = s[2]

    print()
    for i in results :
        print(i)

if __name__=='__main__':
    main()
