import sys
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())
INF = float('inf')

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,cost = map(int,input().split())
    graph[a].append([b,cost]) # a 번 노드에서 b로 가는 비용이 cost

start,end = map(int,input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) #(비용(거리),노드 번호)
    distance[start] = 0 
    # 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택택
    while q:
        curCost,curNode = heapq.heappop(q)
        if distance[curNode] < curCost: # 이 경우 방문한 노드임
            continue
            #end 인덱스 노드에 대한 최단 거리만 요하기 때문에 값 구하면 바로 break
        if curNode ==  end:
                break

        for i in graph[curNode]:
            cost = curCost + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

print(distance[end])



