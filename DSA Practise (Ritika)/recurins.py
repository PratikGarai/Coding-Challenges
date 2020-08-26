def isort(l,k):
    if k>1:
        print("Actual recur",l,k-1)
        isort(l,k-1)
        print()
        print("recur",l,k-1)
        insert(l,k-1)
        print("insert",l,k-1)

def insert(l,k):
    pos=k
    while pos>0 and l[pos]<l[pos-1]:
        (l[pos],l[pos-1])=(l[pos-1],l[pos])
        pos=pos-1
l=[35, 23, 26, 46, 40, 39, 41, 52]
k=len(l)
isort(l,k)
print(l)
