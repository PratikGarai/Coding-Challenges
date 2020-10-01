def process():
    a,b,c,d = list(map(int, input()))

    if (a+b)%2:
        if b>0 and a==0 :
            print("Tidak Ya", end=" ")
        elif b==0 and a>0 :
            print("Ya Tidak", end=" ")
        elif b>0 and a>0 :
            print("Ya Ya", end=" ")
        print("Tidak Tidak")

    else :
        print("Tidak Tidak",  end=" ")
        if d>0 and c==0 :
            print("Tidak Ya")
        elif d==0 and c>0 :
            print("Ya Tidak")
        elif d>0 and c>0 :
            print("Ya Ya")

def main():
    for i in range(int(input())):
        process()

if __name__=='__main__':
    main()
