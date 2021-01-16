arr = []
count = 0

def runningMedian(a):
    global count,arr
    num = a[-1]
    insertInArray(num, count)
    count += 1
    
    if count%2==1 :
        return  arr[count//2]
    else :
        return  (arr[count//2]+arr[(count//2)-1])/2

def insertInArray(n,h):
    global arr
    
    if h==0:
        arr.append(n)
        return
    low = 0
    high = count
    while(low<high):
        mid = (low+high)//2
        #print(mid)
        if n<=arr[mid]:
            high = mid
        elif n>arr[mid]:
            low = mid + 1
    
    arr.insert(low, n)

    
if __name__ == '__main__':
    a_count = int(input())
    a = []
    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)
        result = runningMedian(a)
        print(result)
