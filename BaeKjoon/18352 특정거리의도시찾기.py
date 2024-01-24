import sys
input=sys.stdin.readline

N,M,K,X=map(int,input().split())
graph=[[] for _ in range(N+1)] 
distance=[[0] for _ in range(N+1)]

for i in range(M):
    a,b=map(int, input().split())
    graph[a].append(b)

# print(distance)
# print(graph)

def bfs(graph, start):
    q=[]
    visited=set()
    # 이걸 안넣줘서 끝의 노드가 다시 출발지로 연결되는 엣지가 있는 경우 떄문에 안되었음.
    visited.add(start)

    q.append(start)
    while q:
        now=q.pop(0)
        for neighbor in graph[now]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
                distance[neighbor][0]=distance[now][0]+1
                # print(f'q : {q} ,now: {now},neigbor: {neighbor},dis:{dis}, distance: {distance}')
                if distance[neighbor][0]>K:
                    break


bfs(graph,X)
ans=[]

for i in range(len(distance)):
    if distance[i][0]==K:
        ans.append(i)

ans.sort()

if not ans:
    print(-1)
else:
    for i in range(len(ans)):
        print(ans[i])
        