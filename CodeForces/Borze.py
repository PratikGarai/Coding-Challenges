d = {
        "." : 0,
        "-." : 1,
        "--" : 2
}

s = input()
k = ""

for i in s :
    k += i
    if k in d :
        print(d[k], end="")
        k = ""

print()
