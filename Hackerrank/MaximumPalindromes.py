def factorial(n):
    if n==0 or n==1:
        return 1
    f = 1
    for i in range(2,n+1):
        f *= i
    return f

def process(st):
    a = [0 for i in range(26)]
    for i in st:
        a[ord(i)-97] += 1
    
    se = 0
    odd = 0
    numerator = 1
    denominator = 1
    for i in a:
        if i!=0:
            if i%2 :
                odd += 1
                if i>2:
                    se += i-1
                    denominator *= factorial(i//2)
            else :
                se += i
                denominator *= factorial(i//2)
    numerator = factorial(se//2)
    if odd>1:
        numerator *= odd
    print(numerator//denominator)

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
