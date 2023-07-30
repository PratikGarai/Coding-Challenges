def calculateFactorial(N):
    LEN = 1200
    ans = [0 for i in range(LEN)]
    
    zeros = 0
    rind = LEN - 1
    
    ans[LEN-1] = 1
    for i in range(1, N+1) :
        mul = i
        while mul % 10 == 0 and mul != 0 :
            mul = mul // 10
            zeros += 1
        
        if mul == 0 or mul == 1 : 
            continue
            
        balance = 0
        for j in range(LEN-1, -1, -1) :
            prod = (mul * ans[j]) + balance
            ans[j] = prod%10
            balance = prod//10
            if balance == 0 and j < rind and ans[j] == 0 : 
                rind = j
                break
    
    ind = 0
    for i in range(LEN) :
        ind += 1
        if ans[ind] != 0 :
            break
    
    s = ""
    for i in range(ind, LEN) :
        s += str(ans[i])
    s += "0" * zeros
    return s
