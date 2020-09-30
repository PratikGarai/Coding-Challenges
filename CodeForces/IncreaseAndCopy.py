def process():
    n = int(input())

    if n==1:
        print(0)
        return 0 
    moves = 100000000
    p = int(n**0.5)+1
    for i in range(p-10, p+10):
        if i>0 and i<=n:
            m =(i-2)+n/i
            if(m%1!=0):
                m += 1
            moves = min(moves, m)

    # return int(moves)
    print(int(moves))

def main():
    # res = []
    for i in range(int(input())):
        # res.append(process())
        process()

    # for i in res :
    #     print(i)

if __name__=='__main__':
    main()
