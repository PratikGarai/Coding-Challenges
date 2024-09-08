def main():
     n, k, l, c, d, p, nl, np  = list(map(int, input().split()))
     total_drink = k*l
     total_limes = c*d
     total_salt = p

     print(int(min(int(total_drink/nl), total_limes, int(total_salt/np))/n))

if __name__=='__main__':
    main()
