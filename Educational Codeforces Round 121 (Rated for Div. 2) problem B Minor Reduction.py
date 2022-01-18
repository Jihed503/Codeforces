for i in range(int(input())):
    n = input()
    idx = 0;
    for i in range(len(n)-1):
        if int(n[i])+int(n[i+1]) > 9:
            idx = i
    print(n[:idx]+str(int(n[idx])+int(n[idx+1]))+n[idx+2:])