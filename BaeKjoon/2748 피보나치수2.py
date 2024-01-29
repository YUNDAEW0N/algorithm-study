import sys
input=sys.stdin.readline


N=int(input())

dp=[0]*(N+1)
dp[1]=1
for i in range(2,N+1):
    dp[i]=dp[i-1]+dp[i-2]


print(dp[N])



def dp_fibo(n):
    dp = [0] * (n+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n]
