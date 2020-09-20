def main():
    s = input()
    l = len(s)
    for i in range(int(input())):
        b,g = list(map(int, input().split()))
        if b==g:
            print(1)
        elif b==g-1 and s[b-1]!=s[g-1]:
            print(2)
        elif b==g-1 and s[b-1]==s[g-1]:
            print(1)
        else :
            process(s[b-1:g])

if __name__ == '__main__':
    main()
