import sys
input=sys.stdin.readline

N=int(input())

dp=[0]*(N+2)
arr=[(0,0)]
for i in range(N):
    t,p=map(int,input().split())
    arr.append((p,t))

for i in range(1,N+1):
    dp[i]=max(dp[i],dp[i-1])
    if i+arr[i][1]<=N:   
        dp[i+arr[i][1]]=dp[i] + arr[i][0]

if arr[N][1]==1:
    dp[N]+=arr[N][0]
        
print(dp[N])
  
    