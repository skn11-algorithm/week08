import sys
import heapq
input=sys.stdin.readline
INF=1e8

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start)) # 지금까지 비용, 현재 위치
    distance[start]=0

    while q:
        cost,now=heapq.heappop(q)
        for i in graph[now]:
            new_cost=cost+i[1]
            if new_cost<distance[i[0]]:
                distance[i[0]]=new_cost
                heapq.heappush(q,(new_cost,i[0]))
                

V,E=map(int,input().rstrip().split())
start=int(input().rstrip())
graph=[[] for _ in range(V+1)]
distance=[INF]*(V+1)

for _ in range(E):
    s,e,l=map(int,input().rstrip().split())
    graph[s].append((e,l))#도착지점,자신부터 도착지점까지의 비용

dijkstra(start)
for i in distance[1:]:
    print(i if i<INF else "INF")

