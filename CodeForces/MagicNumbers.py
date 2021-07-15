def main():
    n = input().split("1")
    for i in n :
        if len(i)>2:
            return False
        if not (i=="4" or i=="44" or i==""):
            return False
    return True

n = main()
if n:
    print("YES")
else :
    print("NO")
