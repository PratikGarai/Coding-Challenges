def gcd(a, b):
    if b==0:
        return a
    else :
        return gcd(b, a%b)

def solve() :
    a = input()
    b = input()
    l1 = len(a)
    l2 = len(b)

    lcm = l1*l2//gcd(l1, l2)
    
    if a*(lcm//l1)==b*(lcm//l2):
        return a*(lcm//l1)
    else :
        return -1


if __name__=="__main__":
    t = int(input())
    for i in range(t):
        print(solve())
