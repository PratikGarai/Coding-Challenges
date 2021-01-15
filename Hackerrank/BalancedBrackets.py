def main():

    s = input()
    #print(s)
    stck = []
    
    for i in s :
        if i=='[' or i=='{' or i=='(':
            #print(stck)
            stck.append(i)
        else :
            if stck==[]:
                print("NO")
                return  
            k = stck[-1]
            #print("Here", str(stck) ,k,end="\n", sep="   ")
            stck = stck[:-1]
            if (k=="{" and  i=="}") or (k=="[" and  i=="]") or (k=="(" and  i==")"):
                continue
            else :
                print("NO")
                return
                    
    
    if stck==[]:
        print("YES")
    else :
        print("NO")
        

if __name__=='__main__':
    n = int(input())
    for i in range(n):
        main()
