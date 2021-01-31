n,t = map(int,input().split())
s = [i for i in input()]

for j in range(t):
    i = 0
    while(i<n-1):
        if s[i]=="B" and s[i+1]=="G":
            s[i], s[i+1] = "G", "B"
            i += 2
            if i>=n-1:
                break
        else :
            i+=1

print("".join(s))
