def check(n):
    k = [ i for i in str(n) ]
    return len(set(k))==4

n = int(input())
done = False

while not done:
    n += 1
    if check(n):
        print(n)
        break
