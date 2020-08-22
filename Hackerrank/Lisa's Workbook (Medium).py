N, K = map(int, input().split())
T = list(map(int, input().split()))

cnt = 0 # special problems
i = 0   # chapter number
j = 1   # page number
m = 1   # problem number

while i < N:
    if m <= j and j <= min(m + K - 1, T[i]):
        cnt += 1
    j += 1
    m += K
    if m > T[i]: # next chapter
        i += 1
        m = 1
print(cnt)
    
'''
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

num1=[i+1 for i in range(len(arr))]
count=dict(zip(num1,arr))

j=(1,0)
for i in range(1,len(book)+1):
    
    if (i>1)
        j=(book[i-1][1],book[i-1][0])
    
    if (book[i][1]==j):
        if i in range(1,book[i][0]+1):
            c+=1
        if i in range(1,book[i][0])

print(c)
'''
