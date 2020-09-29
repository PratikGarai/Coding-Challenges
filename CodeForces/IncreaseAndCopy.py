def process():
    n = int(input())

    if n==1:
        return 0 

    moves = 0
    val = 1
    i = 1
    mx_ele = 1
    while val<n:
        moves += 1
        if(i==1):
            i = 0
            mx_ele += 1
            val += 1
        else :
            i = 1
            val += mx_ele
    return moves

def main():
    res = []
    for i in range(int(input())):
        res.append(process())

    for i in res :
        print(i)

if __name__=='__main__':
    main()
