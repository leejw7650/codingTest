from sys import stdin
import heapq

input = stdin.readline()

INF = int(1e9)

n, m = map(int, stdin.readline().split())

start = int(stdin.readline())

graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m) :
    a, b, c = map(int, stdin.readline().split())

    graph[a].append((b,c))

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1) :
    if distance[i] == INF :
        print("INFINITY")
    else :
        print(distance[i])