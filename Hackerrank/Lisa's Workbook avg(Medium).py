nk=input().split()
n=int(nk[0])
k=int(nk[1])
arr=list(map(int,input().split()))
prob=[]; c=0
for i in range(n):
    if arr[i]>k:
        copy=k
        while(copy<=(arr[i]-(arr[i]%k))):
            prob.append((k,i+1))
            copy+=k
        if ((arr[i]%k)>0):
            prob.append((arr[i]%k,i+1))
    else:
        prob.append((arr[i],i+1))
num=[i+1 for i in range(len(prob))]
book=dict(zip(num,prob))

num=[i+1 for i in range(len(arr))]
count=dict(zip(num1,arr))

'''for i in range(1,len(count)+1):
    

    
print(c)'''
