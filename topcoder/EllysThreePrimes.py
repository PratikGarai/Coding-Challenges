# Some theory :
#     1. Every composite number is a product of 2 coprimes. So, if there is a small prime that can 
#        factorize it, there exists a bigger number that pairs up with it.
#     2. In that case, the greatest possible pair of factors a number can have is its square root.
#        All other pairs are formed with one number smaller than it(sq. root) and one larger.
#     3. So, for checking for prime, the shortest method would be to iterate overall primes lesser
#        or equal to the square root of a number. This can save a lot of iterations.

import time 

def get_primes_till(limit):
    l = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]    # list of all primes
    for i in range(54,limit+1):
        prime = True
        sq_root = int(i**0.5)
        for j in l:            # iterating only through the smaller primes
            if(j>sq_root):     # upto the square root only
                break
            if(i%j==0):      
                prime = False
                break
        if prime:
            l.append(i)
    return l

def sum_satisfier():
    return pass

def genrate_triplets(start, end, primes_list, sums_list):
    l = []
    return [0,0,0]

def get3(a):
    primes_list = get_primes_till(1000)  #since upper limit is 10^6, we use all primes till 10^3
    return genrate_triplets(10000,99999,primes_list,a)

def main():
    a = []
    for i in range(5):
        a.append(int(input()))
    start = time.time()
    for i in get3(a):
        print(i,end="\t")
    print()
    end = time.time()
    print("Time : ",(end-start))

if __name__=='__main__':
    main()
