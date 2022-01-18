for i in range(int(input())):
    n = int(input())
    l = list(map(int,input().strip().split()))
    for i in range(1,n-1):
        if l[i]!= l[i-1] and l[i]!= l[i+1]:
            print(i+1)
            break
    else:
        if l[0]!=l[1]:
            print(1)
        else: print(n)