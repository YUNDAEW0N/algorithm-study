# 분할 정복 1

# 정수의 거듭 제곱
# 실수 a와 음이 아닌 정수 b에 대해 a의b제곱을 구하는 문제

#b=0이면 직접 해결 (a의 0승은 1)
#b>=1이면 더 작은 문제로 나눠서 해결
 #b가 짝수면  a의 b/2제곱 x a b/2 제곱
 #b가 홀수면  a의 b-1/2 제곱 x a의 b-1/2제곱 x a


import sys

input = sys.stdin.readline
# sys.setrecursionlimit(10**8)

a, b = list(map(int, input().split()))

def Pow(a: int, b: int):
    if b == 0:
        return 1
    temp = Pow(a, b // 2)
    if b % 2 == 0:
        return temp * temp
    else:
        return temp * temp * a

result = Pow(a, b)
print(result)

