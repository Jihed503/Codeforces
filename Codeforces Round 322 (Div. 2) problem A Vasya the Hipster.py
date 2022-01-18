a,b = map(int,input().split())
if abs(a-b) % 2==0 :
    print(str(min(a,b))+' '+str(abs(a-b)//2))
else :
    print(str(min(a,b))+' '+str((abs(a-b)-1)//2))