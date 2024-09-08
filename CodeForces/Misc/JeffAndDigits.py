n = int(input())
s = list(map(int, input().split()))

n0, n5 = 0, 0
for i in s :
    if i==0:
        n0 += 1
    else :
        n5 += 1

if n0==0:
    print(-1)
elif n5<9:
    print(0)
else :
    n5 = n5-n5%9
    print("5"*n5+"0"*n0)
