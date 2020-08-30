def main():
    s = input()
    n = 0
    count = 0
    for i in s:
        if i=='(':
            n+=1
        elif i==')':
            if n==0:
                count += 1
            else :
                n-=1
    count += n
    print(count)

if __name__=='__main__':
    main()
