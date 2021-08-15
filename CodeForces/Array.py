n = int(input())
arr = list(map(int, input().split()))

neg,pos = 0,0

for i in arr:
    if i<0 :
        neg += 1
    elif i>0:
        pos += 1

arr = sorted(arr)
print("1", arr[0])
if pos==0:
    print("2", arr[1], arr[2])
else :
    print("1", arr[-1])
if pos==0:
    print(n-3, end=" ")
    for i in arr[3:]:
        print(i, end=" ")
else:
    print(n-2, end=" ")
    for i in arr[1:-1]:
        print(i, end=" ")
