def process(a,b):
    a = a.lower()
    b = b.lower()
    l = len(a)
    for i in range(l):
        if ord(a[i])<ord(b[i]):
            print("-1")
            return
        if ord(a[i])>ord(b[i]):
            print("1")
            return
    print("0")


a = input()
b = input()
process(a,b)
