import sys
import heapq

input=sys.stdin.readline
INF=int(1e9)

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start)) #현재까지 거리, 현재 위치
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]:
        #graph[i]에 (도착위치,i에서 도착위치까지의 지름길 길이)
            if i[0]>D: # 도착위치가 고속도로 길이 넘어가면 pass
                continue
            new_cost=dist+i[1]
            if new_cost<distance[i[0]]:
                distance[i[0]]=new_cost
                heapq.heappush(q,(new_cost,i[0]))

N,D=map(int,input().rstrip().split()) # 지름길 개수, 고속도로 길이
graph = [[] for _ in range(D+1)] 
distance=[INF]*(D+1)

for i in range(D+1):
    graph[i].append((i+1,1)) # i->i+1 까지의 비용은 1

for i in range(N):
    start,end,length=map(int,input().rstrip().split()) # 시작위치, 도착위치, 지름길 길이
    if end>D :
        continue
    graph[start].append((end,length)) # 지름길 추가

dijkstra(0)
print(distance[D])