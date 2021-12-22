def encode(arr):
    # Code here
    s = ""
    last = ""
    count = 0
    for i in arr : 
        if i!=last : 
            if last!="" :
                s += last + str(count)
            last = i
            count = 1
        else :
            count += 1
    
    s += last + str(count)
    return s
