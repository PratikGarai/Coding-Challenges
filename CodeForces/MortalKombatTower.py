def process():
    n = int(input())
    a = list(map(int, input().split()))
    
    i = 1
    points = 0
    while(i<n):
        while(i<n):
            if a[i]==1:
                break
            i += 1

        count_1 = 0
        while(i<n):
            if a[i]==0:
                break
            count_1 += 1
            i += 1
        points += count_1//3

    if a[0]==1:
        points += 1

    # print("result : ",points)
    print(points)

def main():
    for i in range(int(input())):
        process()

if __name__=='__main__':
    main()
