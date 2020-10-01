from itertools import combinations
n,k = map(int,input().split())
teams = [list(map(int,list(input()))) for i in range(n)]
sums = [sum([x[0] or x[1] for x in list(zip(*i))]) for i in combinations(teams,2)]
print(max(sums),sums.count(max(sums)),sep='\n')

'''
N=list(map(int,input().split()))
n=N[0]
m=N[1]
l=[]
max=0
c=0
val=[]
for i in range(n):
    l.append(int(input(),2))
for i in range(n):
    for j in range(n):
        val.append(l[i]|l[j])
        if (i!=j  and max<(l[i]|l[j])):
            max=(l[i]|l[j])
            #print(bin(max),bin(l[i]),bin(l[j]))
            cnt=bin(max).count('1')
            
ppl=val.count(max)
print(cnt)
print(int(ppl/2))
'''
