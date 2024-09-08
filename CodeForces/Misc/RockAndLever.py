def process():
    n = int(input())
    l = list(map(int, input().split()))

    counts = [ 0 for i in range(32) ]
    
    for i in l :
        if i==0:
            count[0] += 1
        else:
            counts[len(bin(i))-1]+=1

    count = 0
    for i in counts:
        if i!=0:
            count += (i*(i-1))//2
    print(count)

def main():
    for i in range(int(input())):
        process()
    
if __name__=='__main__':
    main()
