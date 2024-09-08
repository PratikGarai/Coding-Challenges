def process():
    n, m = list(map(int, input().split()))

    flag = 0
    for i in range(n):
        tile = []
        tile.append(list(input().split()))
        tile.append(list(input().split()))
        if (tile[0][1]==tile[1][0]):
            flag = 1

    if m%2 :
         print('NO')
    elif flag :
        print('YES')
    else :
        print('NO')

def main():
    for i in range(int(input())):
        process()

if __name__=='__main__':
    main()
