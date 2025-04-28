import heapq
import sys
input = sys.stdin.read
data = input().split()
idx = 0

V, E = int(data[idx]), int(data[idx+1])
idx += 2
K = int(data[idx])
idx += 1

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = int(data[idx]), int(data[idx+1]), int(data[idx+2])
    idx += 3
    graph[u].append((v, w))

INF = int(1e9)
distance = [INF] * (V+1)
distance[K] = 0
q = [(0, K)]

while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for next_node, cost in graph[now]:
        new_dist = dist + cost
        if new_dist < distance[next_node]:
            distance[next_node] = new_dist
            heapq.heappush(q, (new_dist, next_node))

for d in distance[1:]:
    print(d if d != INF else "INF")
