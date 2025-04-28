import sys
input = sys.stdin.readline
MAX = float('inf')

N, M = map(int, input().split())
edge_mat = [[MAX]*N for _ in range(N)] # 직접 연결한 도로 정보
dist_mat = [[MAX]*N for _ in range(N)] # 최단 거리 정보
ans = [[0]*N for _ in range(N)] # 결과 저장용 행렬 

for _ in range(M) :
  a, b, c = map(int, input().split())
  edge_mat[a-1][b-1] = edge_mat[b-1][a-1] = c # 양방향 도로
  dist_mat[a-1][b-1] = dist_mat[b-1][a-1] = c # 초기 거리 정보 복사사

# k: 경유지, i: 출발지, j: 도착지
for k in range(N) :
  dist_mat[k][k] = 0 # 자기 자신으로의 거리는 0
  for i in range(N-1) :
    for j in range(i+1, N) :
      if j == k or i == k :
        continue 
      if dist_mat[i][j] > dist_mat[i][k] + dist_mat[k][j] :
        dist_mat[i][j] = dist_mat[j][i] = dist_mat[i][k] + dist_mat[k][j]

for i in range(N) :
  for j in range(N) :
    if i == j :
      ans[i][j] = '-' # 같은 노드면 - 표시 
      continue
    for k in range(N) :
      if i == k or edge_mat[i][k] == MAX :
        continue
      if edge_mat[i][k] + dist_mat[k][j] == dist_mat[i][j] :
        ans[i][j] = k+1
        break

for _ans in ans :
  print(*_ans)