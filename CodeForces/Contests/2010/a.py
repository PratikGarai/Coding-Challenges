def alternate_sum(a):
    s = 0
    for i in range(len(a)):
        if i%2==0:
            s += a[i]
        else:
            s -= a[i]
    return s

if __name__=="__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(alternate_sum(a))