def get_keytaps(target_set, key_capacity):
    le = len(target_set)
    if le>sum(key_capacity):
        return -1
    target_set = sorted(target_set, reverse=True)
    key_capacity = sorted(key_capacity)
    return 0

def main():
    target_set = list(map(int,input().split()))
    key_capacity = list(map(int,input().split()))
    print(get_keytaps(target_set,key_capacity))

if __name__=='__main__':
    main()
