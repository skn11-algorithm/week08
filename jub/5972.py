import sys
import heapq

input = sys.stdin.readline
n,m = map(int,input().split())

INF = float("inf") # 무한대 상수 
graph = [[] for _ in range(n+1)] # 그래프 리스트 선언 
distance = [INF] * (n+1) # 처음에는 각 지점의 거리를 무한대로 distance 노드 개수만큼 초기화 

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(s):
    q = [] 
    distance[s] = 0 # 자기자신과의 거리는 0으로 초기화 
    heapq.heappush(q,(0,s)) # (거리, 위치)
    while q: 
        dist, cur = heapq.heappop(q) 
        if distance[cur] < dist: # 이미 계산돼 있는 최솟값보다 크다면 다음 반복으로 넘어감
            continue 
        for next in graph[cur]: # 이웃돼 있는 노드를 확인
            cost = dist + next[1] # dist 출발 지점에서 현재 노드까지의 거리 + 현재 노드에서 다음 노드까지의 거리
            if cost < distance[next[0]]: # 이미 계산돼 있는 최솟값이 더 작았다면 갱신
                distance[next[0]] = cost 
                heapq.heappush(q,(cost, next[0])) 
    return distance[n]

print(dijkstra(1))