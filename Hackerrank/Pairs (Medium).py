nk = list(map(int,input().split()))
n=nk[0];
k=nk[1];
arr=list(map(int,input().split()))
l=[]
c=0
arr.sort()
for i in range(n):
    for j in range(n):
        if abs((arr[i]-arr[j])==k) and ([arr[j],arr[i]] not in l) and ([arr[j],arr[i]] not in l):
            c+=1
            l.append([arr[i],arr[j]])
            
print(c)
