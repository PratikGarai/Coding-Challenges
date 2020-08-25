n=int(input())
arr=list(map(int,input().split()))
l=[]
li=[]
arr.sort()

m=10000000
for i in range(0,n-1):
    m=min(m,abs(arr[i]-arr[i+1]))

for i in range(0,n-1):
    if m==abs(arr[i]-arr[i+1]):
        li.append(arr[i])
        li.append(arr[i+1])

print(*li, sep=" ")



