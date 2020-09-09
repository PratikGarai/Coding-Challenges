def factorial(n):
    p = 1
    for i in range(1,n+1):
        p *= i
    return p

def get_permutatuions(a,b,c,d):
    if (a+b)>(c+d):
        return 0
    if (a+b)==0:
        return 1
    return int(factorial(c+d)/(factorial(c+d-a-b)*factorial(c)*factorial(d)))

def is_valid(n,m):
    for i in range(10):
        if i==2 or i==5 or i==6 or i==9:
            continue
        if n[i]>m[i]:
            return False
    return True

def get_list(s):
    l = [0 for i in range(10)]
    for i in s:
        l[ord(i)-48] += 1
    return l

def main():
    n = input()
    m = input()
    nd = get_list(n)
    md = get_list(m)
    if is_valid(nd, md):
        print(get_permutatuions(nd[2],nd[5],md[2],md[5])*get_permutatuions(nd[6],nd[9],md[6],md[9]))
    else:
        print(0)

if __name__=='__main__':
    main()
