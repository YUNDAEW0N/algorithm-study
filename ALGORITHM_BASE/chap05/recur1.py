# 순수한 재귀 함수 구현하기

def recur(n: int)->int:
    if n>0:
        recur(n-1)
        print(n)
        recur(n-2)



x=int(input())

recur(x)