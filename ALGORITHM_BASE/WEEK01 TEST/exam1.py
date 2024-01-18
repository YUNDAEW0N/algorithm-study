# WEEK01 TEST
import sys
input=sys.stdin.readline

# 1 1110 더하기 사이클

T=int(input())
num=T
count=0


for i in range(99):
  
    x=(num//10)+num%10
    if x>=10:
        num=(num%10)*10+(x%10)
    else:
        num=(num%10)*10+x

    count+=1
    if num==T:
        break

# print(count)

#정답 돌아감


#2 1182 부분수열의 합


n, target=map(int,input().split())
arr=list(map(int,input().split()))
count=0

#하나씩 묶었을 때
for i in range(n):
    if arr[i]==target: count+=1
    for j in range(1,n):
        if arr[i]+arr[j]==target:
            count+=1

#두개씩 묶었을 때
for i in range(n):
    for j in range(n):
        if arr[i+1]!=[None]:
            sum=arr[i]+arr[i+1]
            if sum+arr[j]==target:
                count+=1


# 이런느낌인데 재귀로 접근해야할듯?

print(count)





#3 1992 쿼드트리

#문제를 이해 못하겠음

