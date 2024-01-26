import sys
input=sys.stdin.readline

N,K=map(int,input().split())

graph = []
flag = [[False]*N for _ in range(N)]
visited=[[0]*N for _ in range(N)]

for i in range(N):
   a,b,c=map(int,input().split())
   graph.append([a,b,c])

S,X,Y=map(int,input().split())
second=S




def bfs(si,sj):
    q=[]
    q.append((si,sj))
    if visited[si][sj]==0:
        visited[si][sj]=graph[si][sj]
    while q:
        print(q)
        ci,cj=q.pop(0)
        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj=di+ci,dj+cj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0:
                # q.append((ni,nj))
                if visited[ni][nj]<visited[ci][cj]:
                    visited[ni][nj]=visited[si][sj]
                

count=0

while count<S:
    for i in range(K):
        for j in range(K):
                bfs(i,j)
                print(visited)
            
    count+=1
    print('---------------')






