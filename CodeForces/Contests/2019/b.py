def solve() :
    n, q = map(int, input().split())
    coords = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    left = 0
    right = 1

    counts = {}

    while right < n:
        # center
        elements = coords[right]- coords[left] -1
        if elements != 0 :
            n_ranges = (left+1) * (n-right)
            # print(f"{coords[left]} -> {coords[right]} in {n_ranges} ranges")
            if n_ranges in counts:
                counts[n_ranges] += elements
            else :
                counts[n_ranges] = elements

        # self
        n_ranges = n-1 + left*(n-right)
        # print(f"{coords[left]} in {n_ranges} ranges")
        if n_ranges in counts:
            counts[n_ranges] += 1
        else :
            counts[n_ranges] = 1

        left += 1
        right += 1
    
    # last element
    n_ranges = n-1 + left*(n-right)
    if n_ranges in counts:
        counts[n_ranges] += 1
    else :
        counts[n_ranges] = 1
    # print(f"{coords[left]} in {n_ranges} ranges")
    # print(counts)
    res = []
    for q in queries:
        if q in counts:
            res.append(counts[q])
        else:
            res.append(0)
    
    print(" ".join(map(str, res)))

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__=="__main__":
    main()