def min_counter(a,n):

def main():
    n = int(input())
    a = list(map(int, input().split()))
    t = int(input())
    for i in range(t):
        s = list(map(int, input().split()))
        if s==[2]:
            result = min_counter(sorted(a), n)
        else :
            a[s[1]-1] = s[2]

if __name__=='__main__':
    main()
