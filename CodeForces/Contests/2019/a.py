def solve() :
    n = int(input())
    a = list(map(int, input().split()))

    score = 0

    for ind, i in enumerate(a):
        if n % 2 == 0 :
            score = max(score, n//2 + i)
        else :
            if ind % 2 == 0 :
                score = max(score, (n+1)//2 + i)
            else :
                score = max(score, n//2 + i)
    
    print(score)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__=="__main__":
    main()