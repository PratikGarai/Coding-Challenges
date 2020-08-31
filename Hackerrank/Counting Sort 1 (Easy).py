n=int(input())
a=list(map(int,input().split()))
zero=[0]*100
for i in a:
    zero[i]+=1
print(*zero,sep=" ")
