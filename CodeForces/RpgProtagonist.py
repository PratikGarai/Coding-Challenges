def get_results():
    cap1 , cap2 = list(map(int, input().split()))
    n1, n2  = list(map(int, input().split()))
    w1, w2 = list(map(int, input().split()))

    max_w = 0 
    
    if w2<w1 :                      #setting them in order
        n1, n2 = n2, n1
        w1, w2 = w2, w1

    for your_lighter in range(0, min(n1, cap1//w1)+1):
        your_heavier = min(n2, (cap1-your_lighter*w1)//w2)
        follower_lighter = min(n1-your_lighter, cap2//w1)
        follower_heavier = min(n2-your_heavier, (cap2-follower_lighter*w1)//w2)

        max_w = max(max_w, your_lighter+your_heavier+follower_lighter+follower_heavier)

    return max_w

def main():
    t = int(input())
    res = []
    for i in range(t):
        print(get_results())
    
if __name__=='__main__':
    main()
