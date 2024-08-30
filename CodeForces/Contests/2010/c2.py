s = input()
l = len(s)

if l < 3 :
    print("NO")
    exit()

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

count = {}
for i in range(l) :
    if s[i] in count :
        count[s[i]] += 1
    else :
        count[s[i]] = 1

if len(count) == 1 :
    print("YES")
    print(s[:l-1])
    exit()

found = False
counter1 = {}
counter2 = {}

for i in range(l1, r1) :
    if s[l1+i] in counter1 :
        counter1[s[l1+i]] += 1
    else :
        counter1[s[l1+i]] = 1
    if s[l2+i] in counter2 :
        counter2[s[l2+i]] += 1
    else :
        counter2[s[l2+i]] = 1

def match(a, b) :
    for key in a :
        if key not in b :
            return False
        if a[key] != b[key] :
            return False
    return True

while l2 >= 1 : 
    # print(l1, r1, l2, r2)
    # print(counter1, counter2)
    if match(counter1, counter2) :
        found2 = True
        for i in range(l1, r1) :
            # print(s[l1+i], s[l2+i], s[r1-i-1], s[r2-i-1])
            if s[l1+i] == s[l2+i] and s[r1-i-1] == s[r2-i-1] :
                continue
            else :
                found2 = False
                break
        if found2 :
            found = True
            print("YES")
            print(s[l1:r1])
            break
    
    l2 -= 1
    r1 += 1
    if s[l2] in counter2 :
        counter2[s[l2]] += 1
    else :
        counter2[s[l2]] = 1
    
    if s[r1-1] in counter1 :
        counter1[s[r1-1]] += 1
    else :
        counter1[s[r1-1]] = 1

if not found :
    print("NO")