import sys

from queue import PriorityQueue
INF=int(1e9)

input=sys.stdin.readline


V,E=map(int,input().split())  # V는 노드갯수 E는 엣지갯수
K=int(input())  # 출발지

distance=[INF]*(V+1)  #거리정보 저장 리스트
visited=[False]*(V+1) #방문여부 저장 리스트
graph=[[] for _ in range(V+1)] # 엣지정보 저장 리스트
q=PriorityQueue() # 우선순위 큐

for i in range(E):
    s, e, w = map(int,input().split())
    graph[s].append([e,w])


def dijkstra(graph, start):
    q.put((0,start)) # 출발노드 큐에 넣고 시작
    distance[start]=0 # 거리리스트의 출발 노드 값을 0으로 설정

    while q:
        current=q.get()   # 우선순위 큐에서 노드 가져오기
        c_v=current[1]    
        if visited[c_v]:  # 현재 선택된 노드가 방문한적있으면 continue
            continue
        visited[c_v]=True    # 방문체크
        for temp in graph[c_v]:  # 현재 선택노드의 엣지 정보
            next_node=temp[0]    # 다음 노드
            next_weight=temp[1]  # 다음 노드의 가중치
            if distance[next_node] >distance[c_v]+next_weight:
                distance[next_node]=distance[c_v]+next_weight
                q.put((distance[next_node],next_node))
    return distance


dijkstra(graph,K)

for i in range(1,V+1):
    if distance[i]!=INF:
        print(distance[i])
    else:
        print("INF")
