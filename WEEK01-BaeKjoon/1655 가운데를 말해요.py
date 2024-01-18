from typing import MutableSequence
import heapq
import sys
input=sys.stdin.readline



T=int(input())
s=[]

for i in range(T):
    n=int(input())
    s.append(n)


maxheap=[]
minheap=[]
answer=[]

for i in range(len(s)):
    if len(maxheap)==len(minheap):
        heapq.heappush(maxheap,-s[i]) 
    elif len(maxheap) > len(minheap):
        heapq.heappush(minheap,s[i])
    
    if minheap and minheap[0]>-maxheap[0]:
        answer.append(-maxheap[0])
    elif minheap and minheap[0]<-maxheap[0]:
        answer.append(minheap[0])
    elif minheap and minheap[0]==-maxheap[0]:
        answer.append(minheap[0])


    
       

# print(answer)


for i in range(len(answer)):
    print(answer[i])



# 직접 구현한 최대힙 재구성 heapify를 써서 maxheap을 구하고
# heapq에 있는 minheap 을 써서 했더니 시간초과가 난다. ㅠ