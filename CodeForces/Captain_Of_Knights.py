def process_f(x, y):
    if(x==y):
        return (x-1)//4
    diff_max = max(x-1, y-1)
    diff_min = min(x-1, y-1)

def process():
    x, y, n, m = list(map(int, input().split()))
    f = process_f(x,y)

    for i in range(

def main():
    for i in range(int(input())):
        process()

if __name__ == '__main__':
    main()
