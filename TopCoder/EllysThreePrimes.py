import time 

def get_primes_till(limit):
    l = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]    
    for i in range(54,limit+1):
        prime = True
        sq_root = int(i**0.5)
        for j in l:            
            if(j>sq_root):     
                break
            if(i%j==0):      
                prime = False
                break
        if prime:
            l.append(i)
    return l

def get_primes_from_list(start, end, primes_list):
    l = []
    for i in range(start, end+1):
        prime = True
        sq_root  = int(i**0.5)
        for j in primes_list:
            if(j>sq_root):
                break
            if(i%j==0):
                prime = False
                break
        if prime :
            l.append(i)
    return l

def get_third(first, second, sums_list, digits):
    s = 0
    c_multiplier = 10 
    p_multiplier = 1  
    for i in range(digits) :
        digit = sums_list[i]-(int((first%c_multiplier)/p_multiplier)+int((second%c_multiplier)/p_multiplier))
        if digit<0 or digit>9:
            return -1
        s += digit*p_multiplier
        p_multiplier, c_multiplier = c_multiplier, c_multiplier*10
    return s

def generate_triplets(start, end, primes_list, sums_list):
    l = get_primes_from_list(start, end, primes_list)
    le = len(l)

    def check_presence(n) :   
        low , high = 0, le-1
        while low<=high :
            mid = int((low+high)/2)
            if l[mid]==n:
                return True
            elif l[mid]>n:
                high = mid-1
            else:
                low = mid+1
        return False

    # test code
    # if(20533 in l and 44927 in l and 87179 in l):
    #     print("Prime list check")
    # if(check_presence(20533)):
    #     print("Binary search check 1")
    # if(check_presence(44927)):
    #     print("Binary search check 2")
    # if(check_presence(87179)):
    #     print("Binary search check 3")
    # if(get_third(20533,44927,sums_list,5)==87179):
    #     print("Generation correct ",get_third(20533,44927,sums_list,5))
    # else :
    #     print("Generation incorrect ",get_third(20533,44927,sums_list,5))

    for i in range(le):
        for j in range(i+1,le):
            third = get_third(l[i], l[j], sums_list,5)
            if(third==-1):
                continue
            if check_presence(third):
                return [l[i], l[j], third]
    return []

def get3(a):
    primes_list = get_primes_till(1000)  
    return generate_triplets(10000,99999,primes_list,a)

def main():
    a = list(map(int, input().split()))
    start = time.time()
    for i in get3(a):
        print(i,end="\t")
    print()
    end = time.time()
    print("Time : ",(end-start))

if __name__=='__main__':
    main()


# TEST CASES
#-------------------------------
# Case 1 : 
# 19 12 15 11 14
# 10007   42643   99989
# Time :  0.06131744384765625
#-------------------------------
# Case 2 : (worst case)
# 22 19 3 8 23

# Time :  22.881287574768066
#-------------------------------
