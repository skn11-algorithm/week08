import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())
INF = int(1e9)
distance = [INF] * (n+1)
distance[start] = 0
q = [(0, start)]

while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for nxt, cost in graph[now]:
        if distance[nxt] > dist + cost:
            distance[nxt] = dist + cost
            heapq.heappush(q, (distance[nxt], nxt))

print(distance[end])
