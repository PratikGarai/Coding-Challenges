def get_cost(arr, num):
    s = 0
    for ind, i in enumerate(arr):
        s += abs(num**ind - i)
    return s

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    max_cost = get_cost(arr, 1)
    high_limit = int(max_cost**(1/(n-1)))+1
    
    min_cost = max_cost
    for i in range(2, 2*high_limit+1):
        min_cost = min(min_cost,get_cost(arr, i))

    print(min_cost)

if __name__=='__main__':
    main()
