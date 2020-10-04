def biggerIsGreater(w):
    control=list(w)
    c1=' '
    c2=' '
    for count,char in reversed(list(enumerate(w))):
        c1=char
        if ord(c2)>ord(c1) and c2!=' ':
            minord=26
            char=c1
            for counter,item in enumerate(w[count:]):
                if ord(item)-ord(char)<minord and ord(item)>ord(char):
                    minord=ord(item)-ord(char)
                    rem=counter
            control=control[count:]
            print(control[rem])
            control.pop(rem)
            control=w[:count]+w[count+rem]+''.join(sorted(control))
            break
        c1,c2=c2,c1
    if control==list(w):
        return('no answer')
    else:
        return(''.join(control))


