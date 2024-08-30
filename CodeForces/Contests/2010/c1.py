s = input()
l = len(s)

l1 = 0
r1 = 0
l2 = 0
r2 = 0

if l%2 == 0 :
    l1 = 0
    r2 = l
    l2 = l//2-1
    r1 = l//2+1
else :
    l1 = 0
    r2 = l
    l2 = l//2
    r1 = l//2 + 1

found = False

while l2 >= 1 : 
    if s[l1] == s[l2] :
        if s[l1:r1] == s[l2:r2] :
            found = True
            print("YES")
            print(s[l1:r1])
            break
    l2 -= 1
    r1 += 1

if not found :
    print("NO")