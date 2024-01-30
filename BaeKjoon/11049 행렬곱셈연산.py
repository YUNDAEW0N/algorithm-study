import sys
input=sys.stdin.readline

T=int(input())


matrix=[[]]
for i in range(T):
    row,col=map(int,input().split())
    matrix.append((row,col))

dp=[[-1]*(T+1) for _ in range(T+1)]

print(matrix)
print(dp)

def excute(s,e):
    result=int(1e9)
    
    #이미 계산되어있으면 바로 리턴
    if dp[s][e]!=-1:
        return dp[s][e]
    # 행렬이 하나면 연산 필요 없음
    if s==e:
        return 0
    # 행렬이 2개면 N*M*K
    if s+1==e:
        return matrix[s][0]*matrix[s][1]*matrix[e][0]
    
    #행렬이 3개 이상일때
    for i in range(s,e):
        a=matrix[s][0]*matrix[i][1]*matrix[e][0]
        # D[s][e]=D[s][i] + D[i+1][e] + a
        result=min(result,excute(s,i)+ excute(i+1,e)+ a)

    
    return result


print(excute(1,T))