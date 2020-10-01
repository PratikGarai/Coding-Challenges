n=int(input())
a=list(map(int,input().split()))
zero=[0]*100
for i in a:
    zero[i]+=1
for i in range(100):
    while(zero[i]!=0):
        print(i, end=" ")
        zero[i]-=1
