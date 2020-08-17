def superDigit(x, n):
    res=sum([int(i) for i in x])
    if (res*n<10):
        return res*n
    else:
        return superDigit(str(res*n),1)
print(superDigit('9875',4))
