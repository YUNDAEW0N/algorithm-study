import sys
input=sys.stdin.readline

T=int(input())

arr=[[0]*T for _ in range(T)]
dp=[[()]*T for _ in range(T)]

for i in range(T):
    arr[i]=list(map(int, input().split()))

count=0
for i in range(T):
    for j in range(T):   
        dp[i][j]+=(i+arr[i][j],j),(i,j+arr[i][j])
        if dp[i][j][0]==(T-1,T-1) or dp[i][j][1]==(T-1,T-1):
            count+=1



print(count-1)