def process(a, b, step):

    if(a==b):
        return step
    steps = a+b
    changed = False
    if(a>b):
        if(a%5==0):
            val = process(a//5, b, step+1)
            if val!=-1:
                steps = min(steps, val)
                changed = True
        elif(a%3==0):
            val = process(a//3, b, step+1)
            if val!=-1:
                steps = min(steps, val)
                changed = True
        elif(a%2==0):
            val = process(a//2, b, step+1)
            if val!=-1:
                steps = min(steps, val)
                changed = True
        else :
            return -1
    else:
        if(b%5==0):
            val = process(a, b//5, step+1)
            if val!=-1:
                steps = min(steps, val)
                changed = True
        elif(b%3==0):
            val = process(a, b//3, step+1)
            if val!=-1:
                steps = min(steps, val)
                changed = True
        elif(b%2==0):
            val = process(a, b//2, step+1)
            if val!=-1:
                steps = min(steps, val)
                changed = True
        else :
            return -1
    if not changed:
        return -1
    else :
        return steps

    

a,b = map(int, input().split())
print(process(a,b,0))
