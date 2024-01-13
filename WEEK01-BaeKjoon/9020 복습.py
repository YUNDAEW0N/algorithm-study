# 안보고 직접 짜보기


import math

def is_prime(N):
    if N==0:
        return False
    for i in range(2,int(math.sqrt(N))+1):
        if N%i==0:
            return False
    return True


T=int(input())


for i in range(T):
    n=int(input())

    a= n//2
    b= n//2

    for i in range(n//2):
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a-=1
            b+=1