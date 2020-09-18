def get_result():
    x,y,k = list(map(int,input().split()))

    coals = k
    sticks_for_coals = y*k
    sticks_needed = k
    total_sticks_needed = sticks_for_coals+sticks_needed

    trades_for_sticks = (total_sticks_needed-1 )//(x-1)
    if ((total_sticks_needed-1)/(x-1))%1 != 0 :
        trades_for_sticks += 1
    trades_for_coals = k

    return trades_for_sticks+trades_for_coals

def main():
    t = int(input())
    for i in range(t):
        print(get_result())

if __name__=='__main__':
    main()
