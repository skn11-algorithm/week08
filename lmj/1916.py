# 최소비용 구하기 
'''
입력 : 도시의 개수N / 버스의 개수 M / 버스의 정보 (출발도시 번호, 도착도시 번호, 버스 비용용) 
출력 : 출발 ~ 도착 도시까지 가는 최소 비용
'''
import heapq, sys
input = sys.stdin.readline
INF = int(1e9) 

n, m = int(input()), int(input())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(1, m + 1):
    a, b, c = map(int, input().strip().split())
    graph[a].append((b, c))

# 간선 정보 입력받기 
start, end = map(int, input().strip().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  
    distance[start] = 0
   
    while q:
        curCost, curNode = heapq.heappop(q)
        
        if distance[curNode] < curCost:
            if curNode == end:
                break
            else:
                continue
        for i in graph[curNode]:
            cost = curCost + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
print(distance[end])