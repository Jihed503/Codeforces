from math import sqrt
def premier(n):
    prime_flag = 0
  
    
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        return True
    else:
        return False
    
 
 
for i in range(int(input())):
    n = int(input())
    s = 0
    i = 1
    ch = ""
    while i<10**9 and s < n:
        i+=1
        if premier(i):
            ch += str(i) + ' '
            s += 1
    print(ch.strip())