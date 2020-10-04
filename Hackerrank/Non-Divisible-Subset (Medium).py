def nonDivisibleSubset(k, s):
    a=s.copy()
    rem=[]
    countem={}
    div=[]
    ans=0
    for x in range(0,k):
        countem[x]=0
    for number in s:
        rem.append(number%k)
    for number in list(set(rem)):
        countem[number]=rem.count(number)
    if(k%2==0):
        for t in range(1,int(k/2)):
            ans+=max(countem[t],countem[k-t])
        if(countem[k/2]>0):
            ans+=1
    else:
        for t in range(1,(k//2)+1):
            ans+=max(countem[t],countem[k-t])
    if(countem[0]>0):
        ans+=1
    return ans
