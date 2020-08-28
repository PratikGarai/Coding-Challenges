n= int(input())
a= list(map(int,input().split()))

m=0
count=[0]*6
for i in a:
    count[i]+=1

print(count.index(max(count)))
