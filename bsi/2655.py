# INCOMPLETE
from collections import deque

def min_black_to_white(grid, n):
    # 상하좌우 이동을 위한 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 방문 체크 및 최소 변환 횟수 저장 배열
    # 초기값을 무한대로 설정
    visited = [[float('inf')] * n for _ in range(n)]
    
    # 덱 초기화 (시작 위치: (0, 0))
    queue = deque([(0, 0, 0)])  # (x, y, 변환 횟수)
    visited[0][0] = 0
    
    while queue:
        x, y, changes = queue.popleft()
        
        # 현재 위치가 이미 더 적은 변환으로 방문한 적이 있다면 스킵
        if changes > visited[x][y]:
            continue
        
        # 끝방에 도달했다면 현재까지의 변환 횟수 반환
        if x == n-1 and y == n-1:
            return changes
        
        # 모든 방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 바둑판 범위 내에 있는지 확인
            if 0 <= nx < n and 0 <= ny < n:
                # 흰 방인 경우 (가중치 0)
                if grid[nx][ny] == 1:
                    if changes < visited[nx][ny]:
                        visited[nx][ny] = changes
                        # 가중치 0인 간선은 큐의 앞에 추가
                        queue.appendleft((nx, ny, changes))
                # 검은 방인 경우 (가중치 1)
                else:
                    if changes + 1 < visited[nx][ny]:
                        visited[nx][ny] = changes + 1
                        # 가중치 1인 간선은 큐의 뒤에 추가
                        queue.append((nx, ny, changes + 1))
    
    # 끝방에 도달할 수 없는 경우 (이 문제에서는 발생하지 않음)
    return -1

# 입력 처리
n = int(input())
grid = []
for _ in range(n):
    row = list(map(int, list(input().strip())))
    grid.append(row)

# 결과 출력
result = min_black_to_white(grid, n)
print(result)