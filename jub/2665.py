from collections import deque
import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
input = sys.stdin.readline

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
cnt = [[1e9]*n for _ in range(n)]

# 0-1 BFS 구현을 위한 덱 사용
queue = deque()
queue.append((0, 0))
cnt[0][0] = 0

while queue:
    x, y = queue.popleft()  # 가장 적은 비용의 노드 먼저 처리
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            # 흰 방인 경우 (비용 0)
            if arr[nx][ny] == '1' and cnt[nx][ny] > cnt[x][y]:
                cnt[nx][ny] = cnt[x][y]
                queue.appendleft((nx, ny))  # 우선순위 높음
            # 검은 방인 경우 (비용 +1)
            elif arr[nx][ny] == '0' and cnt[nx][ny] > cnt[x][y] + 1:
                cnt[nx][ny] = cnt[x][y] + 1
                queue.append((nx, ny))  # 우선순위 낮음

print(cnt[n-1][n-1])
