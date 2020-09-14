def get_results():
    cap1 , cap2 = list(map(int, input().split()))
    n1, n2  = list(map(int, input().split()))
    w1, w2 = list(map(int, input().split()))

    total_weight = n1*w1 + n2*w2
    if(total_weight<=cap1 or total_weight<=cap2):
        return (cap1+cap2)

    max_w = 0
    
    for i in range(cap1//w1):                       #my sword
        for j in range(cap2//w1):                   #follower sword

            #check number of swords
            if (i+j)>n1:
                break
            for k in range(cap1//w2):               #my axe
                for l in range(cap2//w2):           #follower axe

                    #check number of axes
                    if (k+l)>n2:
                        break

    return max_w

def main():
    t = int(input())
    for i in range(t):
        print(get_results())

if __name__=='__main__':
    main()
