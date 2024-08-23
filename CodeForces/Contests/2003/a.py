def check_string(l, s) :
    if s[0] == s[-1] :
        return "No"
    else :
        return "Yes"

if __name__ == "__main__" :
    t = int(input())
    for i in range(t) :
        l = int(input())
        s = input()
        res = check_string(l, s)
        print(res)