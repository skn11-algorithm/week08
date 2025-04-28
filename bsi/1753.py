import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())  # 시작 정점

# 그래프 생성 (정점 개수에 맞게 크기 설정)
graph = [[] for _ in range(V+1)]

# 간선 정보 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # u에서 v로 가는 가중치 w인 간선

# 다익스트라 알고리즘
def dijkstra(start):
    # 최단 거리 배열
    distances = [float('inf')] * (V+1)
    distances[start] = 0
    
    # 우선순위 큐 초기화 (거리, 정점)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)
        
        # 이미 처리된 정점이라면 스킵
        if current_dist > distances[current_vertex]:
            continue
        
        # 인접한 정점 확인
        for next_vertex, weight in graph[current_vertex]:
            new_dist = current_dist + weight
            
            # 더 짧은 경로를 찾았다면 업데이트
            if new_dist < distances[next_vertex]:
                distances[next_vertex] = new_dist
                heapq.heappush(priority_queue, (new_dist, next_vertex))
    
    return distances

# 시작 정점에서 모든 정점까지의 최단 거리 계산
result = dijkstra(K)

# 결과 출력
for i in range(1, V+1):
    if result[i] == float('inf'):
        print("INF")
    else:
        print(result[i])