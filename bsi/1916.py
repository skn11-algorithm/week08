# import sys
# import heapq
# input = sys.stdin.readline

# lst = []
# n = int(input())
# m = int(input())
# for _ in range(m):
#     start, end, cost = map(int, input().split())
#     lst.append((start, end, cost))

# desti_start, desti_end = map(int, input().split())
     

# def dij(lst, desti_end):
#     total = set([0, desti_end])

#     for start, end, cost in lst:
#         total.add(start)
#         total.add(end)

#     total = sorted(list(total))

#     graph = {pos: [] for pos in total} 

#     for i in range(len(total)-1):
#         current, next = total[i], total[i+1]
#         graph[current].append((next, next - current))

#     for start, end, cost in lst:
#         graph[start].append((end, cost))

#     ways = {pos: float('inf') for pos in total}
#     ways[0] = 0
#     priority = [(0, start)]

#     while priority:
#         current_distance, current_position = heapq.heappop(priority)

#         if current_distance > ways[current_position]:
#             continue
           
#         for neighbor, distance in graph[current_position]:
#             new_distance = current_distance + distance

#             if new_distance < ways[neighbor]:
#                 ways[neighbor] = new_distance
#                 heapq.heappush(priority, (new_distance, neighbor))
                
#             if new_distance == desti_end:
#                 break
#     return ways[cost]

# result = dij(lst, desti_end)
# print(result)

import sys
import heapq

input = sys.stdin.readline

# 도시 개수 입력
n = int(input())
# 버스 개수 입력
m = int(input())

# 그래프 생성
graph = [[] for _ in range(n+1)]

# 버스 정보 입력
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))  # 출발 도시에서 도착 도시로 가는 비용

# 출발 도시와 도착 도시 입력
start_city, end_city = map(int, input().split())

# 다익스트라 알고리즘
def dijkstra(start, end):
    # 최소 비용 저장 배열
    distances = [float('inf')] * (n+1)
    distances[start] = 0
    
    # 우선순위 큐 초기화 (비용, 도시)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_cost, current_city = heapq.heappop(priority_queue)
        
        # 이미 처리된 도시라면 스킵
        if current_cost > distances[current_city]:
            continue
            
        # 목적지에 도달했다면 종료
        if current_city == end:
            return current_cost
        
        # 인접한 도시 확인
        for next_city, bus_cost in graph[current_city]:
            new_cost = current_cost + bus_cost
            
            # 더 저렴한 경로를 찾았다면 업데이트
            if new_cost < distances[next_city]:
                distances[next_city] = new_cost
                heapq.heappush(priority_queue, (new_cost, next_city))
    
    return distances[end]

# 최소 비용 계산 및 출력
result = dijkstra(start_city, end_city)
print(result)