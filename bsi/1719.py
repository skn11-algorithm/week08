# import sys
# import heapq

# input = sys.stdin.readline
# N, M = map(int, input().split())

# # 그래프 생성
# graph = [[] for _ in range(N+1)]

# # 양방향 간선 추가
# for _ in range(M):
#     A, B, C = map(int, input().split())
#     graph[A].append((B, C))  # A에서 B로 가는 길에 C마리의 소
#     graph[B].append((A, C))  # B에서 A로 가는 길에 C마리의 소 (양방향)

# # 다익스트라 알고리즘으로 최소 여물 경로 찾기
# def dijkstra(start, end):
#     # 최소 여물 기록
#     min_feed = [float('inf')] * (N+1)
#     min_feed[start] = 0
    
#     # 우선순위 큐 초기화 (누적 여물, 현재 위치)
#     priority_queue = [(0, start)]
    
#     while priority_queue:
#         current_feed, current_pos = heapq.heappop(priority_queue)
        
#         # 이미 더 적은 여물로 도달 가능하면 스킵
#         if current_feed > min_feed[current_pos]:
#             continue
            
#         # 목적지에 도달했으면 종료
#         if current_pos == end:
#             return current_feed
        
#         # 인접한 헛간 탐색
#         for next_pos, cows in graph[current_pos]:
#             next_feed = current_feed + cows
            
#             # 더 적은 여물로 갈 수 있다면 업데이트
#             if next_feed < min_feed[next_pos]:
#                 min_feed[next_pos] = next_feed
#                 heapq.heappush(priority_queue, (next_feed, next_pos))
    
#     return min_feed[end]

# # 모든 쌍에 대한 최소 여물 계산
# # lstlst를 제대로 초기화
# lstlst = [[0 for _ in range(N+1)] for _ in range(N+1)]

# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if i == j:
#             lstlst[i][j] = 0  # 자기 자신으로 가는 비용은 0
#         else:
#             lstlst[i][j] = dijkstra(i, j)

# # 결과 출력
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         print(lstlst[i][j], end=" ")
#     print()  # 줄바꿈
# 시간초과

import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한대 값 설정

# 입력 받기
n, m = map(int, input().split())  # 집하장 개수 n, 경로 개수 m

# 거리 행렬과 경로 행렬 초기화
dist = [[INF] * (n+1) for _ in range(n+1)]  # 거리 행렬
next_node = [[0] * (n+1) for _ in range(n+1)]  # 경로표 행렬

# 자기 자신으로 가는 거리는 0으로 초기화
for i in range(1, n+1):
    dist[i][i] = 0

# 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())  # a에서 b로 가는 비용이 c
    dist[a][b] = c  # 양방향 그래프
    dist[b][a] = c
    next_node[a][b] = b  # a에서 b로 가기 위해 처음 방문할 노드는 b
    next_node[b][a] = a  # b에서 a로 가기 위해 처음 방문할 노드는 a

# 플로이드-와샬 알고리즘
for k in range(1, n+1):  # 중간 노드
    for i in range(1, n+1):  # 시작 노드
        for j in range(1, n+1):  # 도착 노드
            if dist[i][j] > dist[i][k] + dist[k][j]:  # 더 짧은 경로 발견
                dist[i][j] = dist[i][k] + dist[k][j]
                next_node[i][j] = next_node[i][k]  # i에서 j로 가기 위해 처음 방문할 노드 갱신

# 경로표 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:  # 자기 자신으로 가는 경우
            print("-", end="")
        else:
            print(next_node[i][j], end="")
        
        # 마지막 열이 아니면 공백 출력
        if j < n:
            print(" ", end="")
    print()  # 줄바꿈