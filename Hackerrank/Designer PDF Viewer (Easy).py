li=list(map(int,input().split()))
string=input()
al=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
res=dict(zip(al,li))
maxi=0
for i in string:
    if res[i]>maxi:
        maxi=res[i]
print(len(string)*maxi)


