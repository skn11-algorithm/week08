# 택배 배송

'''
입력 : N개의 헛간, M개의 소의 길 / 헛간 A_i, B_i, C_i마리의 소
출력 : 현서가 가져가야 할 최소 여물의 수
아이디어 : 시작 지점이 주어지고, 최단거리 -> 다익스트라 (항상 작은값을 가져야 하므로 우선순위 큐를 사용)
'''

import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)] 
distance = [INF] * (n+1) 

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(s):
    q = [] 
    distance[s] = 0
    heapq.heappush(q,(0,s))
    while q: 
        dist, now = heapq.heappop(q) 
        if distance[now] < dist: 
            continue 
        for next in graph[now]: 
            cost = dist + next[1]
            if cost < distance[next[0]]: 
                distance[next[0]] = cost 
                heapq.heappush(q,(cost, next[0]))
    return distance[n]

print(dijkstra(1))




