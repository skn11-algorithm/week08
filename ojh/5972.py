import sys
import heapq

input=sys.stdin.readline
INF=1e8

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start)) # 현재까지 걸린 비용, 현재 위치
    distance[start]=0

    while q:
        cost,now=heapq.heappop(q)
        if now>N:
            continue
        for i in graph[now]: # i : (도착지점,도착까지의 비용)
            new_cost=cost+i[1]
            if new_cost<distance[i[0]]:
                distance[i[0]]=new_cost
                heapq.heappush(q,(new_cost,i[0]))

N,M=map(int,input().rstrip().split())
graph=[[] for _ in range(N+1)]
distance=[INF]*(N+1)

for _ in range(M):
    s,e,l=map(int,input().rstrip().split())
    # 양방향 처리
    graph[s].append((e,l))
    graph[e].append((s,l))

dijkstra(1)
print(distance[N])



