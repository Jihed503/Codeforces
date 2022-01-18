for t in range(int(input())):
    n = int(input())
    ch = input()
    lch = list(ch[::-1])
    oper = int(lch[0])
    lch[0] = '0'
    while(lch!=['0']*n):
        for i in range(1,len(lch)):
            if lch[i] !='0':
                oper += int(lch[i])+1
                lch[i] = '0'
    print(oper)