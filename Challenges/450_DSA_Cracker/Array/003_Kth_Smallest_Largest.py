def kthSmallLarge(arr, n, k):
    
    arr = sorted(arr)
    return arr[k - 1], arr[n -k]    

