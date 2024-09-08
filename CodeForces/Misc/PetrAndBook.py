n = int(input())
s = list(map(int, input().split()))
ind = 0
while(n>0):
    n -= s[ind]
    if n<=0:
        break
    ind += 1
    if ind==7 :
        ind = 0
print(ind+1)
