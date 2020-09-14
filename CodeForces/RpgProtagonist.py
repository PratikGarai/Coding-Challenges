def get_results():
    cap1 , cap2 = list(map(int, input().split()))
    n1, n2  = list(map(int, input().split()))
    w1, w2 = list(map(int, input().split()))

    total_weight = n1*w1 + n2*w2
    if(total_weight<=cap1 or total_weight<=cap2):
        return (n1+n2)

    max_w = 0
    
    for i in range((cap1//w1)+1):                       #my sword
        for j in range((cap2//w1)+1):                   #follower sword

            #check number of swords
            if (i+j)>n1:
                break
            for k in range((cap1//w2)+1):               #my axe

                #check my capacity
                if (i*w1+k*w2)>cap1:
                    break
                for l in range((cap2//w2)+1):           #follower axe

                    #check number of axes
                    if (k+l)>n2:
                        break
                    #check follower capacity
                    if (j*w1+l*w2)>cap2:
                        break
                    #the real deal
                    if (i+j+k+l)>max_w:
                        max_w = i+j+k+l

    return max_w

def main():
    t = int(input())
    res = []
    for i in range(t):
        res.append(get_results())
    
    for i in res:
        print(i)

if __name__=='__main__':
    main()
