# 지름길

'''
* 입력 : 지름길 개수 N과 고속도로 길이 D / 지름길의 시작위치, 도착위치, 지름길의 길이
* 출력 : 운전해야 할 거리의 최솟값
* 아이디어 : 
    - 지름길을 찾기 위해 다익스트라에 최소 힙을 사용해 최단거리를 찾는다
    -  heappush(q, (우선순위, 값))
    -  우선순위 heap은 

         (2, 'B')
        /        \
    (5, 'A')     (4, 'C')

    이런식으로 루트노드에 최솟값을 가진다 

'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, d = map(int,input().split())
graph = [[] for _ in range(d+1)]
distance = [INF] * (d+1)


for i in range(d):
    graph[i].append((i+1,1))

for _ in range(n):
    start, end , length = map(int, input().split())
    if end > d: 
        continue
    
    #지름길 정보 입력
    graph[start].append((end, length))

def dijkstra(start):
    q = [] 
    heapq.heappush(q, (0,start))    
    distance[start] = 0    
    
    while q:
        dist, now = heapq.heappop(q)    # 현재 가장 거리가 짧은 노드 pop 
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]  # 현재 지점에서 길/지름길을 더함 

            # 해당 노드로 가는데 계산된 비용이 최단거리테이블보다 작으면 업데이트
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(0)
print(distance[d])