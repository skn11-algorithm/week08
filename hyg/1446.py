import sys, heapq

n, d = map(int, sys.stdin.readline().split())
inf = float("inf")

graph = [[] for _ in range(d+1)]
dist = [inf]*(d+1)

for i in range(d):
    graph[i].append((i+1, 1))

for _ in range(n):
    start, dest, length = map(int, sys.stdin.readline().split())
    if dest<=d:
        graph[start].append((dest, length))

q = []
heapq.heappush(q, (0,0))
dist[0] = 0

while q:
    w1, u = heapq.heappop(q)

    for v, w2 in graph[u]:
        cost = dist[u] + w2
        if dist[v] > cost:
            dist[v] = cost
            heapq.heappush(q, (cost, v))
print(dist[d])