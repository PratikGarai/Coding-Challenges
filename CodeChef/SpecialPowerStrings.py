import time 

def make_dict(string):
    d  = {}
    for i in range(97,123):
        d[chr(i)] = 0
    for i in string :
        if i not in ('#','!','?'):
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
    diff = subs_dict(d1,d2)
    l = len(diff)
    if l==0:
        return 0
    ds = get_set(diff)
    hs = get_set(hx)
    qs = get_set(qm)
    es = get_set(ex)

    if len(ds-hs)==0 or len(ds-qs)==0 or len(ds-es)==0:
        return 1
    if len(ds-(hs|qs))==0 or len(ds-(qs|es))==0 or len(ds-(hs|es))==0:
        return 2
    if len(ds-(hs|qs|es))==0:
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
