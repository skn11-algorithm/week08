import sys
import heapq

input = sys.stdin.readline
N, M = map(int, input().split())

# 그래프 생성
graph = [[] for _ in range(N+1)]

# 양방향 간선 추가
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))  # A에서 B로 가는 길에 C마리의 소
    graph[B].append((A, C))  # B에서 A로 가는 길에 C마리의 소 (양방향)

# 다익스트라 알고리즘으로 최소 여물 경로 찾기
def dijkstra(start, end):
    # 최소 여물 기록
    min_feed = [float('inf')] * (N+1)
    min_feed[start] = 0
    
    # 우선순위 큐 초기화 (누적 여물, 현재 위치)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_feed, current_pos = heapq.heappop(priority_queue)
        
        # 이미 더 적은 여물로 도달 가능하면 스킵
        if current_feed > min_feed[current_pos]:
            continue
            
        # 목적지에 도달했으면 종료
        if current_pos == end:
            return current_feed
        
        # 인접한 헛간 탐색
        for next_pos, cows in graph[current_pos]:
            next_feed = current_feed + cows
            
            # 더 적은 여물로 갈 수 있다면 업데이트
            if next_feed < min_feed[next_pos]:
                min_feed[next_pos] = next_feed
                heapq.heappush(priority_queue, (next_feed, next_pos))
    
    return min_feed[end]

# 농부 현서(헛간 1)에서 농부 찬홍(헛간 N)까지의 최소 여물 계산
result = dijkstra(1, N)
print(result)