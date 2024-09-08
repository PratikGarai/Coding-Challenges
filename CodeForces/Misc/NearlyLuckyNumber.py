n = int(input())
c = 0
while(n != 0):
    r = n%10
    if r==4 or r==7:
        c += 1
    n = n//10

if c==0:
    print("NO")
else :
    d = True
    while(c != 0):
        r = c%10
        if r!=4 and r!=7:
            d = False
            break
        c = c//10
    if not d :
        print("NO")
    else :
        print("YES")
