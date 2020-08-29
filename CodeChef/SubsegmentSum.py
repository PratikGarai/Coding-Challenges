def main():
    n = int(input())
    a = list(map(int, input().split()))
    t = int(input())
    for i in range(t):
        s = list(map(int, input().split()))
        if s==[2]:
            gsum = 0
            s_a = sorted(a)
            count = 0
            for i in range(n):
                count += 1
                try :
                    if s_a[i+1]>s_a[i]+1:
                        gsum += count
                        count = 0
                except :
                    break
            gsum += count
            print("Result : ",gsum)
        else :
            a[s[1]-1] = s[2]

if __name__=='__main__':
    main()
