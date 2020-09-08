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
    print(nd)
    print(md)

if __name__=='__main__':
    main()
