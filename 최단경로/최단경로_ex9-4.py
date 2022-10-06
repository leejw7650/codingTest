import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,m+1) :
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1,n+1) :
    for i in range(1,n+1) :
        for j in range(1,n+1) :
            if graph[i][j] > graph[i][k] + graph[k][j] :
                graph[i][j] = graph[i][k] + graph[k][j]

x, k = map(int, input().split())

if graph[1][k] + graph[k][x] >= INF :
    print(-1)
else :
    print(graph[1][k] + graph[k][x])