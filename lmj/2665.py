# 미로 만들기 : 미로를 찾을 수 있도록 검은 방을 흰 방으로 바꾸기 (바꾸는 방의 갯수를 최소화)
# 검은방0 흰방1
'''
입력 : 한 줄에 들어가는 방의 수 n
출력 : 바꿀 검은방의 수 (최소)
아이디어 : 위아래 양옆을 깊게 탐색 -> 다익스트라? bfs ?

'''

import sys
import heapq
 
n = int(input())
 
graph = [list(map(int, input())) for _ in range(n)]
distance = list([sys.maxsize] * n for _ in range(n))
 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
def dijkstra():
  q = []
  heapq.heappush(q, (0, 0, 0))  # q에 비용, x, y
  distance[0][0] = 0
 
  while q:
    cost, x, y = heapq.heappop(q)
 
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
 
      if 0 <= nx < n and 0 <= ny < n and distance[ny][nx] > cost + 1:
        if graph[ny][nx] == 0:
          distance[ny][nx] = min(distance[ny][nx], cost + 1)    # 벽이면 부수고 
        else:
          distance[ny][nx]= min(distance[ny][nx], cost) # 빈 방일시 통과 
        heapq.heappush(q, (distance[ny][nx], nx, ny))
 
dijkstra()
print(distance[n-1][n-1])


'''
# bfs를 이용한 풀이

from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    visited = [[float('inf')] * N for _ in range(N)]    # 최댓값으로 초기화
    visited[0][0] = 0
    Q = deque([(0, 0, 0)])
    while Q:
        r, c, cnt = Q.popleft()
        if (r, c) == (N-1, N-1):        # 목적지 흰 방에 도달하면 리턴
            print(cnt)
            return
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < N):   # 격자 밖으로 나가면
                continue

            # 이동할 곳이 흰 방일 때 최솟값으로 갱신할 수 있는 곳일 때만 값 갱신
            if maze[nr][nc] == '1' and visited[nr][nc] > visited[r][c]+1:
                visited[nr][nc] = cnt
                Q.appendleft((nr, nc, cnt))

            # 이동할 곳이 검은 방일 때
            if maze[nr][nc] == '0':
                # 이미 방문했다면 최솟값으로 갱신할 수 있는 곳일 때만 값 갱신
                if visited[nr][nc] != float('inf') and visited[r][c] + 1 < visited[nr][nc]:
                    visited[nr][nc] = cnt + 1
                    Q.append((nr, nc, cnt + 1))
                # 아직 방문하지 않았다면 첫 방문이므로 검은 방을 흰 방으로 갱신
               if visited[nr][nc] == float('inf'):
                    visited[nr][nc] = cnt + 1
                    Q.append((nr, nc, cnt + 1))

# main
N = int(input())
maze = [list(input().strip()) for _ in range(N)]
bfs()
'''