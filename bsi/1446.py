import sys
import heapq
input = sys.stdin.readline

n, length = map(int, input().split())
lst = []
for _ in range(n):
    start, end, distance = map(int, input().split())
    if end <= length and end - start > distance:
        lst.append((start, end, distance))

def dij(lst, length):
    total = set([0, length])

    for start, end, distance in lst:
        total.add(start)
        total.add(end)

    total = sorted(list(total))

    graph = {pos: [] for pos in total} 

    for i in range(len(total)-1):
        current, next = total[i], total[i+1]
        graph[current].append((next, next - current))

    for start, end, distance in lst:
        graph[start].append((end, distance))

    ways = {pos: float('inf') for pos in total}
    ways[0] = 0
    priority = [(0, 0)]

    while priority:
           current_distance, current_position = heapq.heappop(priority)

           if current_distance > ways[current_position]:
               continue
           
           for neighbor, distance in graph[current_position]:
               new_distance = current_distance + distance

               if new_distance < ways[neighbor]:
                   ways[neighbor] = new_distance
                   heapq.heappush(priority, (new_distance, neighbor))
    return ways[length]

result = dij(lst, length)
print(result)