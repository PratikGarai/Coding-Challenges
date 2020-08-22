def get_days(d):
    y,m,d = list(map(int,d.split('.')))
    s = d
    s += int((y-1)/4) + y*365
    mnths = [31,28,31,30,31,30,31,31,30,31,30,31]
    s += sum(mnths[:m])
    if m>2 and y%4==0:
        s += 1
    return s

def main():
    a = input()
    b = '2021.07.23'
    ad = get_days(a)
    bd = get_days(b)
    print(bd-ad)

if __name__ == '__main__':
    main()
