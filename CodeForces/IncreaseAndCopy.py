def process():
    n = int(input())

    if n==1:
        return 0 
    
    moves = 0

    return moves

def main():
    res = []
    for i in range(int(input())):
        res.append(process())

    for i in res :
        print(i)

if __name__=='__main__':
    main()
