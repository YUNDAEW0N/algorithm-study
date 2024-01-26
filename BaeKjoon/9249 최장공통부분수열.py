import sys
input=sys.stdin.readline

#인덱스 맞추기 위해 앞에 의미없는 문자 추가. 
s1 = [0]+list(input().rstrip())
s2 = [0]+list(input().rstrip())


dp=[[0]*len(s2) for _ in range(len(s1))]

max_len = 0  # 최장 공통 문자열의 길이
end_index = 0  # 최장 공통 문자열의 끝 인덱스

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i]==s2[j]:
            dp[i][j]=dp[i-1][j-1]+1
            if dp[i][j]>max_len:
                max_len=dp[i][j]
                end_index=i
        else:
            dp[i][j]=0


result = s1[end_index - max_len + 1:end_index + 1]
print(max_len)
print(''.join(result))
