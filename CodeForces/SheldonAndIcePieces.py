def factorial(n):
    p = 1
    for i in range(2,n+1):
        p *= i
    return p

def get_permutatuions(a,b,c):
    return int(factorial(b+c)/(factorial(b+c-a)*factorial(b)*factorial(c)))

def get_dict(s):
    n2,n5,n6,n9 = 0,0,0,0
    for i in s:
        if i=='2':
            n2 += 1
        elif i=='5':
            n5 += 1
        elif i=='6':
            n6 += 1
        elif i=='9':
            n9 += 1
    return (n2,n5,n6,n9)

def main():
    n = input()
    m = input()
    nd = get_dict(n)
    md = get_dict(m)
    print(get_permutatuions(nd[0]+nd[1], md[0], md[1])*get_permutatuions(nd[2]+nd[3], md[2], md[3]))

if __name__=='__main__':
    main()
