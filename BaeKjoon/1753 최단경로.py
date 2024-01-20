import sys
input=sys.stdin.readline
from queue import PriorityQueue

V, E=map(int, input().split())  #V노드갯수 E엣지갯수
K=int(input())  # K= 출발노드
distance=[sys.maxsize]*(V+1)   #거리저장리스트 충분히 큰 값으로
visited=[False]*(V+1)   #방문여부 저장 리스트
myList=[[] for _ in range(V+1)]  #엣지 데이터 저장 인접 리스트
q=PriorityQueue()  #다익스트라를 위한 우선순위 큐


# 인접리스트에 데이터 저장
for _ in range(E):
    u,v,w=map(int, input().split())   # 출발지 도착지 가중치
    myList[u].append((v, w))

q.put((0, K))
distance[K]=0

while q.qsize()>0:
    current=q.get()
    c_v = current[1]
    if visited[c_v]:
        continue
    visited[c_v]=True
    for temp in myList[c_v]:
        next = temp[0]
        value=temp[1]
        if distance[next] > distance[c_v]+value:
            distance[next]=distance[c_v]+value
            q.put((distance[next],next))

for i in range(1,V+1):
    if visited[i]:
        print(distance[i])
    else:
        print('INF')