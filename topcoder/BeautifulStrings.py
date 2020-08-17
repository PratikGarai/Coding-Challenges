def compute(ca,cb,ma,mb):
    if ma==0 or ca==0:
        return mb
    if mb==0 or cb==0:
        return ma
    if ca==cb :
        return 2*ca
    if ca<cb :
        min_groups = ca
        max_groups = ca+2
        max_limit = mb
        max_count = ma
    else :
        min_groups = cb
        max_groups = cb+2
        max_limit = ma
        max_count = ma
    if max_groups*max_limit>=max_count:
        return min_groups+le_final+max_count
    else :
        return min_groups+max_groups*max_count


def main():
    countA = int(input())
    countB = int(input())
    maxA = int(input())
    maxB = int(input())

    print(compute(countA, countB, maxA, maxB))

if __name__ == '__main__':
    main()
