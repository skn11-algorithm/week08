import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

INF = int(1e9)
dist = [INF] * (n+1)
dist[1] = 0

q = [(0, 1)]  # (거리, 현재 노드)
while q:
    cost, now = heapq.heappop(q)
    if dist[now] < cost:
        continue
    for nxt, nxt_cost in graph[now]:
        total_cost = cost + nxt_cost
        if dist[nxt] > total_cost:
            dist[nxt] = total_cost
            heapq.heappush(q, (total_cost, nxt))

print(dist[n])