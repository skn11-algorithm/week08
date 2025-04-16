import sys
import heapq

input=sys.stdin.readline
INF=1e8

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start,[start])) # 현재까지 거리, 시작위치, 지금까지의 경로
    distance[start][start]=0

    while q:
        cost,now,route=heapq.heappop(q)
        if cost>distance[start][now]:
            continue
        for i in graph[now]: # (도착위치,도착까지 거리) (2,3) (3,1)
            new_cost=cost+i[1]
            if new_cost<distance[start][i[0]]:
                distance[start][i[0]]=new_cost
                new_route=route+[i[0]]
                result[start][i[0]]=new_route
                heapq.heappush(q,(new_cost,i[0],new_route))


n,m=map(int,input().rstrip().split())
graph=[[] for _ in range(n+1)]
distance=[[INF]*(n+1) for _ in range(n+1)] 
result=[[[] for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    s,e,l=map(int,input().rstrip().split())
    graph[s].append((e,l))
    graph[e].append((s,l))


for i in range(1,n+1):
    dijkstra(i)

for row in result[1:]:
    for i in row[1:]:
        if i:
            print(i[1],end=' ')
        else:
            print('-',end=' ')
    print()