def interpret(value, commands, args):
    v = value
    for i,j in zip(commands,args):
        if i=='+':
            v += j
        elif i=='*':
            v *= j
        elif i=='-':
            v -= j
        else :
            return -1
    return v

def main():
    print("Enter the initial value : ", end="")
    v = int(input())
    print("Enter the number of commands : ",end="")
    n = int(input())
    c,a = [],[]
    for i in range(n):
        print("Enter the {}th command : ".format(i+1), end="")
        c.append(input())
        print("Enter the {}th argument : ".format(i+1), end="")
        a.append(int(input()))

    print("The result is :", interpret(v,c,a))

if __name__=='__main__':
    main()
