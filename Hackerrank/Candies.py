def candies(n, arr):
    l = len(arr)
    candies = [0 for i in range(l)]
    s = sorted(list(zip(arr, range(l))))
    for i in s:
        if i[1]==0:
            if arr[0]==arr[1]:
                candies[0] = 1
            else :
                candies[0] = candies[1]+1
        elif i[1]==l-1:
            if arr[l-1]==arr[l-2]:
                candies[l-1] = 1
            else :
                candies[l-1] = candies[l-2]+1
        else:
            pos = i[1]
            if arr[pos-1]>=arr[pos] and arr[pos+1]>=arr[pos]:
                candies[pos] = 1 
            elif arr[pos-1]>=arr[pos] and arr[pos+1]<arr[pos]:
                candies[pos] = candies[pos+1]+1
            elif arr[pos-1]<arr[pos] and arr[pos+1]>=arr[pos]:
                candies[pos] = candies[pos-1]+1
            else :
                candies[pos] = max(candies[pos-1], candies[pos+1]) +1
    return sum(candies)

def main():
    n = int(input())
    arr = []
    for i in range(n):
        a = int(input())
        arr.append(a)
    print(candies(n, arr))

if __name__ == '__main__':
    main()
