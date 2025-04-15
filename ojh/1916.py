import sys
import heapq

input=sys.stdin.readline
INF=int(1e9)

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start)) # 현재까지 거리, 현재 위치
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]: # i = (도착지점,i부터 도착까지 비용)
            if i[0]>city:
                continue
            new_cost=dist+i[1]
            if new_cost<distance[i[0]]:
                distance[i[0]]=new_cost
                heapq.heappush(q,(new_cost,i[0]))

city=int(input().rstrip()) # 도시 수
bus=int(input().rstrip()) #버스 수
graph=[[] for _ in range(city+1)]
distance=[INF]*(city+1)

for _ in range(bus):
    start,end,cost=map(int,input().rstrip().split())#출발,도착,비용
    graph[start].append((end,cost))

s_city,e_city=map(int,input().rstrip().split())
dijkstra(s_city)
print(distance[e_city])

