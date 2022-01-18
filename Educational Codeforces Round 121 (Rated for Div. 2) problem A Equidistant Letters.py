for i in range(int(input())):
    ch = input()
    res = ''
    res2 = ''
    for c in ch:
        if ch.count(c) == 1: res += c
        else:
            if c not in res2 : res2 += c
    
    res += res2*2
    print(res)