s = input()

c = 0
for i in s :
    if i.isupper():
        c += 1
    else :
        c -= 1

if c>0:
    print(s.upper())
else :
    print(s.lower())
