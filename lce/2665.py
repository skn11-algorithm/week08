import sys
import heapq
input = sys.stdin.readline

n = int(input())
maze = [list(map(int, input().strip())) for _ in range(n)]
INF = int(1e9)
dist = [[INF]*n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = [(0, 0, 0)]  # (변경 횟수, x, y)
dist[0][0] = 0

while q:
    cnt, x, y = heapq.heappop(q)
    if x == n-1 and y == n-1:
        print(cnt)
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            ncnt = cnt if maze[nx][ny] == 1 else cnt + 1
            if dist[nx][ny] > ncnt:
                dist[nx][ny] = ncnt
                heapq.heappush(q, (ncnt, nx, ny))
