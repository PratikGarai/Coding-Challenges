s=input()
t=input()
k=int(input())

l=min(len(s),len(t))
m=0
i=0

if (len(s)+len(t)<k):
    print("Yes")
    exit()

while(i<l):
    if s[i]!=t[i]:
        break 
    else:
        i+=1
p=len(s)-i
q=len(t)-i

if (p+q<=k and (k-p-q)%2==0):
    print("Yes")
else:
    print("No")
