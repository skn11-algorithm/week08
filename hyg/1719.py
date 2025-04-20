from sys import stdin
from typing import List

INF = 10001

# 플로이드 와샬
def floyd_warshall(n: int, dists: List[List[int]], res: List[List[str]]) -> List[List[str]]:
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    continue
                if dists[i][j] > dists[i][k] + dists[k][j]:
                    dists[i][j] = dists[i][k] + dists[k][j]
                    res[i][j] = res[i][k]
    return res

if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    n, m = map(int, input().split())
    dists = list(([INF] * (n + 1)) for _ in range(n + 1))
    res = [['-'] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        a, b, w = map(int, input().split())
        dists[a][b] = dists[b][a] = w
        res[a][b] = str(b)
        res[b][a] = str(a)

    res = floyd_warshall(n, dists, res)

    for line in res[1:]:
        print(*line[1:], sep=' ')