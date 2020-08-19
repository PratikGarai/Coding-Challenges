import time 

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

def get_set(string):
    s = set()
    for i in string : 
        s.add(i)
    return s

def compute(s1,s2,hx,qm,ex):
    d1 = make_dict(s1)
    d2 = make_dict(s2)
    diff = subs_dict(s1,s2)
    l = len(diff)
    if l==0:
        return 0
    ds = get_set(diff)
    hs = get_set(hx)
    qe = get_set(qm)
    es = get_set(ex)

    if ds-hs=={} or ds-qs=={} or ds-es=={}:
        return 1
    if ds-(hs|qs)=={} or ds-(qs|es) or ds-(hs|es):
        return 2
    if ds-(hs|qs|es):
        return 3
    else: 
        return -1

def main():
    s1 = input()
    s2 = input()
    hx = input()
    qm = input()
    ex = input()
    a = time.time()
    res = compute(s1,s2,hx,qm,ex)
    if res==-1 :
        print('Not possible')
    else :
        print(res)
    b = time.time()
    print()
    print('Computation time : ',(b-a))

if __name__=='__main__':
    main()
