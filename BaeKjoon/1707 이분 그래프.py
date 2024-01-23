import sys
input=sys.stdin.readline

T=int(input())
info=[[] for _ in range(T)]



for i in range(T):
    n,m=map(int,input().split())
    info[i].append([n,m])
    for j in range(m):
        u,v=map(int,input().split())
        info[i].append([u,v])


print(info)





def dfs(graph, start):
    visited=[False]*len(graph)
    stack=[start]

    while stack:
        now=stack.pop()
        if not visited:
            visited[now]=True
            stack.extend(reversed(graph[now]))
        
    return visited


