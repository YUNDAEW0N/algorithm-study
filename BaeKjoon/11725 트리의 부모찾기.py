import sys
input=sys.stdin.readline


N=int(input())
graph=[[] for _ in range(N+1)]



for i in range(N-1):
    a, b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(len(graph)):
    graph[i].sort()



#재귀적 dfs
visited=[0]*(N+1)

def dfs(graph,start):
    for i in graph[start]:
        if not visited[i]:
            visited[i]=start
            dfs(graph,i)
            # print(visited)




dfs(graph,1)


for i in range(2,N+1):
    print(visited[i])
    
