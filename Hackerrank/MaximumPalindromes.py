def getRes(counts):
    l = 0
    o = 0
    res = 1
    den = 1
    for i in counts :
        for j in range(1,(i//2)+1):
            res = (res*(l+j)//j)
        l += i//2
        o += i%2
        
    if not o:
        o = 1
    res = o*res
    return res%mod

def main():
    
    s = input()
    l = len(s)
    mat = [[0 for i in range(l)] for j in range(l)]
    
    for begin in range(l):
        counts = [0 for i in range(26)]
        mat[begin][begin] = 1
        counts[ord(s[begin])-97] += 1
        for end in range(begin+1,l):
            ind = ord(s[end])-97
            counts[ind] += 1
            mat[begin][end] = getRes(counts)
    
    t = int(input())
    for i in range(t):
        l,r = map(int, input().split())
        print(mat[l-1][r-1]%mod)

main()
