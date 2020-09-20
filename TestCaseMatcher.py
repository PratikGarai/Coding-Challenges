def main():
    print("Enter the number of test cases")
    n = int(input())
    t1 = []
    t2 = []
    print("\nEnter set 1")
    for i in range(n):
        inp = input()
        while(inp.strip!=""):
            t1.append(inp)
    print("\nEnter set 2")
    for i in range(n):
        inp = input()
        while(inp.strip!=""):
            t2.append(inp)
    c = 0
    for i in range(n):
        if t1[i]!=t2[i]:
            c += 1
    print("Result will be printed in order of input")
    print("\n\n",c," number of mismatches found, show how many? (-1 for all)")
    k = int(input())
    if k==-1 :
        k = c
    for i in range(n):
        if t1[i]!=t2[i]:
            print(t1[i],"\t\t",t2[i])
            k -= 1
        if k<=0:
            break
    print("\n\n Finished ... ")

if __name__=='__main__':
    main()
