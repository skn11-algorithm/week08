import sys
input = sys.stdin.readline

n, d = map(int, input().split())
shortcut = []
for _ in range(n):
    start, end, length = map(int, input().split())
    if end <= d:
        shortcut.append((start, end, length))

distance = [i for i in range(d+1)]

for i in range(d+1):
    if i > 0:
        distance[i] = min(distance[i], distance[i-1] + 1)
    for s, e, l in shortcut:
        if s == i and distance[e] > distance[s] + l:
            distance[e] = distance[s] + l

print(distance[d])
