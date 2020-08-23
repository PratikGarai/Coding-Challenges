an=int(input())
arr=list(map(int,input().split()))
bn=int(input())
brr=list(map(int,input().split()))

test=[arr,brr]
l=[]

a=set(arr)
b=set(brr)


if list(b-a):
    l=list(b-a)
    res=list(set.intersection(*map(set,test)))
    if res:
        for i in res:
            if arr.count(i)!= brr.count(i) and i not in l:
                l.append(i)
    
else:
    res=list(set.intersection(*map(set,test)))
    for i in res:
        if arr.count(i)!= brr.count(i):
            l.append(i)

l.sort()
print(*l,sep=" ")

