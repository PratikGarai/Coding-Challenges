def process():
    n = int(input())
    a = list(map(int, input().split()))
    
    i = 0
    points = 0
    turn = 0                     # 0 => friend  1=> me
    while(i<n):
        if turn==0:
            if a[i]==1 :         #deal with the current enemy atleast
                points += 1
            if i!=n-1 :
                if a[i+1]==0:    #if next boss is easy, defeat it
                    i += 2
                else :           #skip the bass and let mc handle
                    i += 1
            else :               #finish the game
                i += 1
            turn = 1
        else :
            if i!=n-1:
                if a[i+1]==1:    #move 2 steps if next boss is hard
                    i += 2
                else :           #leave easy boss to friend
                    i += 1
            else:                #finish the game
                i += 1
            turn = 0
    # print("result : ",points)
    print(points)

def main():
    for i in range(int(input())):
        process()

if __name__=='__main__':
    main()
