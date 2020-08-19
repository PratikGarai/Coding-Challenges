def get_keytaps(target_set, key_capacity):
    le = len(target_set)
    if le>sum(key_capacity):
        return -1
    buttons = len(key_capacity)
    target_set = sorted(target_set, reverse=True)
    key_capacity = sorted(key_capacity)
    multipliers  = [ 1 for i in range(buttons) ]
    pointer = 0
    keytaps = 0
    for i in range(le):
        keytaps += multipliers[pointer]*target_set[i]
        multipliers[pointer] += 1
        pointer += 1
        if pointer==buttons :
            pointer = 0
    return keytaps

def main():
    target_set = list(map(int,input().split()))
    key_capacity = list(map(int,input().split()))
    print(get_keytaps(target_set,key_capacity))

if __name__=='__main__':
    main()
