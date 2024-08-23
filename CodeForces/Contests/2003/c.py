# Wrong answer in test case 5
# Problem : Use 2 characters with max frequency and alternate them. Single max character (current implementation) is not enough. It may make the characters repeat one after the other if the diff in frequency is more than 2.

from heapq import heapify, heappop, heappush

def check_value(l, a) :
    c = {}
    for i in a :
        if i in c :
            c[i] += 1
        else :
            c[i] = 1

    # No repeating elements
    if max(c.values()) == 1 :
        return a
    # All elements are repeating
    if max(c.values()) == l :
        return a
    
    max_heap = [(-v, k) for k, v in c.items()]
    heapify(max_heap)

    res = []
    prev_char = None
    prev_count = 0

    while max_heap :
        count, char = heappop(max_heap)
        res.append(char)
        count += 1
        if prev_count < 0 :
            heappush(max_heap, (prev_count, prev_char))
        prev_count, prev_char = count, char
    
    return "".join(res)

if __name__=="__main__" :
    t = int(input())
    for i in range(t) :
        l = int(input())
        s = input()
        res = check_value(l, s)
        print(res)