# 유클리드 호제법으로 최대 공약수 구하기

def gcd(x: int,y: int)->int:
    if y==0:
        return x
    else:
        return gcd(y,x%y)

if __name__=='__main__':
    x=int(input())
    y=int(input())

    print(f'{gcd(x,y)}')