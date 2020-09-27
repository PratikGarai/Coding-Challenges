class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self, n, l):
        self.head  = Node(l[0])
        self.length = n
        current = self.head
        for i in l[1:]:
            current.next = Node(i)
            current = current.next

        self.start = None
        self.end = None

    def set_query(self, x, y):
        i = 0
        current = self.head
        while(i<x):
            current = current.next
            i+=1
        self.start = current
        while(i<n-x-y):
            current = current.next
            i+=1
        self.end = current


def main():
    n, q = list(map(int, input().split()))
    l = list(map(int, input().split()))
    ls = List(n,l)

if __name__=='__main__':
    main()
