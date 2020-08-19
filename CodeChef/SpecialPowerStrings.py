def make_dict(string):
    d  = {}
    for i in range(97,123):
        d[chr(i)] = 0
    for i in string and i not in ('#','!','?'):
        d[i] += 1
    return d

def subs_dict(d1, d2):
    s = ''
    for i in range(97,123):
        if d1[chr(i)]-d2[chr(i)]>0:
            s += chr(i)
    return s

def is_covered_by(main, sub):
    pass

def compute(s1,s2,hx,qm,ex):
    d1 = make_dict(s1)
    d2 = make_dict(s2)
    diff = subs_dict(s1,s2)
    if len(diff)==0:
        return 0

def main():
    s1 = input()
    s2 = input()
    hx = input()
    qm = input()
    ex = input()
    print(compute(s1,s2,hx,qm,ex))

if __name__=='__main__':
    main()
