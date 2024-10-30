import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
        self.index_map = {}  # A mapping from element to its index for O(1) access

    def push(self, value):
        heapq.heappush(self.heap, value)
        self.index_map[value] = self.heap.index(value)  # Store index of the new value

    def pop_min(self):
        if not self.heap:
            raise IndexError("pop from an empty heap")
        min_value = heapq.heappop(self.heap)
        del self.index_map[min_value]  # Remove from index map
        return min_value

    def get_min(self):
        if not self.heap:
            raise IndexError("get_min from an empty heap")
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0

    def delete(self, value):
        if value not in self.index_map:
            return

        # Find the index of the value to delete
        index = self.index_map[value]
        # Replace it with the last element in the heap
        last_value = self.heap[-1]
        self.heap[index] = last_value
        self.index_map[last_value] = index  # Update the index map
        
        # Remove the last element
        self.heap.pop()
        del self.index_map[value]  # Remove the deleted value from the index map

        # Restore the heap property
        if index < len(self.heap):
            heapq._siftup(self.heap, index)  # Bubble up
            heapq._siftdown(self.heap, 0, index)  # Bubble down
    

def solve() :
    n, m, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    mp = {}
    for i in range(n) :
        mp[a[i]] = i
    
    first_presentations = [MinHeap() for _ in range(n)]
    for i in range(n):
        first_presentations[i].push(m)

    for i in range(m) :
        ind = mp[b[i]]
        first_presentations[ind].push(i)
    
    state = "YA"
    for i in range(1, n) :
        if first_presentations[i].get_min() < first_presentations[i-1].get_min() :
            state = "TIDAK"
            break
    print(state)

    for _ in range(q) :
        ns, np = map(int, input().split())
        if b[ns-1] == np : 
            print(state)
            continue
        else :
            pp = b[ns-1]
            b[ns-1] = np

            first_presentations[mp[pp]].delete(ns-1)
            first_presentations[mp[np]].push(ns-1)

            state = "YA"
            for i in range(1, n) :
                if first_presentations[i].get_min() < first_presentations[i-1].get_min() :
                    state = "TIDAK"
                    break
            print(state)
            
def main() :
    t = int(input())
    for _ in range(t) :
        solve()

if __name__=="__main__" :
    main()