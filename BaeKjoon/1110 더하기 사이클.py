import sys
input=sys.stdin.readline

T=int(input())
num=T
count=0


while True:
  
    x=(num//10)+num%10
    if x>=10:
        num=(num%10)*10+(x%10)
    else:
        num=(num%10)*10+x

    count+=1
    if num==T:
        break

print(count)