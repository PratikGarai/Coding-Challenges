def maxMin(k, arr):
    arr = sorted(arr)
    l = len(arr)
    if k>l:
        k = l
    if k==l:
        return arr[l-1]-arr[0]
    m = arr[l-1]-arr[0]
    if m==0:
         return 0
    for i in range(0, l-k+1):
        if (arr[i+k-1]-arr[i])<m:
            m = arr[i+k-1]-arr[i]
    return m

def main():
    n = int(input())
    k = int(input())
    arr = []
    for i in range(n):
        a = int(input())
        arr.append(a)
    result = maxMin(k, arr)
    print(result)

if __name__ == '__main__':
    main()
