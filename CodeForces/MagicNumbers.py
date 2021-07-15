def main():
    s = {"1", "14", "144"}
    n = input()

    st = ""
    streak = False
    for i in n :
        if st in s :
            streak = True
        st += i
        if st not in s and not streak:
            return False
        if st not in s :
            st = i
            streak = False
        else :
            streak = True

    return st in s

n = main()
if n:
    print("YES")
else :
    print("NO")
