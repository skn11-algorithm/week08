import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = float('inf')
dist = [[INF]*n for _ in range(n)]
route = [['-']*n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    dist[u][v] = w
    dist[v][u] = w
    route[u][v] = v+1
    route[v][u] = u+1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                route[i][j] = route[i][k]

for r in route:
    print(' '.join(map(str, r)))
