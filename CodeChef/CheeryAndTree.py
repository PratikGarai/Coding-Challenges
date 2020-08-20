def main():
    h,w = list(map(int, input().split()))
    m = [[0 for i in range(w)] for  in range(h)]
    for i in range(h):
        m[h] = list(map(int, input().split()))
    n = int(input())
    results = []
    for i in range(n):
        x1,y1,x2,y2 = list(map(int,input().split()))
        results.append(compute(m,x1,y1,x2,y2))
    for i in results :
        print(i)

if __name__ == '__main__':
    main()
