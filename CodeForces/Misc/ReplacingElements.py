def solve() :
    n, d = map(int, input().split())
    ls = list(map(int, input().split()))

    ls = sorted(ls)
    if (ls[0]+ls[1]<=d) or (ls[-1]<=d): 
        return "YES"
    else :
        return "NO"

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        print(solve())
