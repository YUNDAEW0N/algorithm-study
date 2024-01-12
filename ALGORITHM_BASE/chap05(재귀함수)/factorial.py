# 양의 정수 n의 팩토리얼 구하기

def factorial(n: int) -> int:
    """양의 정수 n의 팩토리얼값을 재귀적으로 구함"""
    if n>0:
        return n*factorial(n-1)
    else:
        return 1
    


if __name__ == '__main__':
    n=int(input())
    print(f'{n}!={factorial(n)}')