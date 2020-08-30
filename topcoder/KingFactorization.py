prime_list = [2]

def check_prime(a):
    global prime_list
    for i in prime_list:
        if(a%i==0):
            return False
    prime_list.append(a)
    return True

def get_mid(n,a,b):
    if a==b :
        return a
    if prime_list[-1]<a:
        prime_list.append(a)
    if(n%a==0):
        return a
    for i in range(a+1, b):
        if check_prime(i):
            if n%i==0 :
                return i
    return b

def compute(n,l):
    le = len(l)
    lst = []
    for i in range(0, le-1):
        lst.append(l[i])
        n = int(n/l[i])
        g = get_mid(n,l[i],l[i+1])
        n = int(n/g)
        lst.append(g)
    #trailing
    g = l[le-1]
    lst.append(g)
    n = int(n/g)
    if prime_list[-1]<g:
        prime_list.append(g)
    if n!=1:
        lst.append(n)
    return lst

def  main():
    n = int(input())
    l = list(map(int, input().split()))
    print(compute(n,l))

if __name__=='__main__':
    main()
