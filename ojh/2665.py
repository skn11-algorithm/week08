import sys
import heapq

input=sys.stdin.readline
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def dijkstra(x,y):
    q=[]
    heapq.heappush(q,(0,x,y)) # 현재까지의 거리, 현재 위치 x,y

    while q:
        cost,x,y=heapq.heappop(q)
        visited[x][y]=True
        if x==n-1 and y==n-1:
            return cost
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if graph[nx][ny]==1 : # 흰방
                    heapq.heappush(q,(cost,nx,ny))
                else: #검은방
                    heapq.heappush(q,(cost+1,nx,ny))
                visited[nx][ny]=True

n=int(input().rstrip())
graph=[]
visited=[[False]*(n) for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int,input().rstrip())))

print(dijkstra(0,0))