def get_res(l, s) :
    s.sort()
    return s[l//2]

if __name__ == "__main__" :
    t = int(input())
    for i in range(t) :
        l = int(input())
        s = list(map(int, input().split()))
        res = get_res(l, s)
        print(res)