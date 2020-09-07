def main():
    s = input()
    le = len(s)
    l = list(zip(s, range(le)))
    l = sorted(l, key = lambda x: (x[0], -x[1]), reverse=True)
    s = l[0][0]
    current_index = l[0][1]
    for i in l[1:]:
        if i[1]>current_index:
            s += i[0]
            current_index = i[1]

    print(s)

if __name__=='__main__':
    main()
