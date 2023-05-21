
class Solution:
    
    def splitter(self, arr, left, right, temp):
        if left>=right-1 : 
            return 0
        mid = (right+left)//2
        count = 0
        count += self.splitter(arr, left, mid, temp)
        count += self.splitter(arr, mid, right, temp)
        count += self.merger(arr, left, mid, right, temp)
        return count
        
    def merger(self, arr, left, mid, right, temp):
        count = 0
        i = left
        j = mid
        ind = left
        while i<mid and j<right:
            if arr[i] <= arr[j] :
                temp[ind] = arr[i]
                ind += 1
                i += 1
            else : 
                temp[ind] = arr[j]
                count += mid-i
                ind += 1
                j += 1
        while i<mid :
            temp[ind] = arr[i]
            i += 1
            ind += 1
        while j<right:
            temp[ind] = arr[j]
            j += 1
            ind += 1
        for i in range(left, right) :
            arr[i] = temp[i]
        return count
    
    def inversionCount(self, arr, n):
        temp = [-1 for i in range(n)]
        return self.splitter(arr, 0, n, temp)
        

