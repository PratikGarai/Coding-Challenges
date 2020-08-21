s=input()
t=input()
k=int(input())

l=min(len(s),len(t))
m=0
i=0
while(i<l):
    if s[i]!=t[i]:
        break 
    else:
        i+=1
p=len(s)-i
q=len(t)-i

if (p+q<=k):
    print("Yes")
else:
    print("No")
