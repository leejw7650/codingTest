# 문제
# 매일 아침, 세준이는 학교에 가기 위해서 차를 타고 D킬로미터 길이의 고속도로를 지난다. 이 고속도로는 심각하게 커브가 많아서 정말 운전하기도 힘들다. 어느 날, 세준이는 이 고속도로에 지름길이 존재한다는 것을 알게 되었다. 모든 지름길은 일방통행이고, 고속도로를 역주행할 수는 없다.

# 세준이가 운전해야 하는 거리의 최솟값을 출력하시오.

# 입력
# 첫째 줄에 지름길의 개수 N과 고속도로의 길이 D가 주어진다. N은 12 이하인 양의 정수이고, D는 10,000보다 작거나 같은 자연수이다. 다음 N개의 줄에 지름길의 시작 위치, 도착 위치, 지름길의 길이가 주어진다. 모든 위치와 길이는 10,000보다 작거나 같은 음이 아닌 정수이다. 지름길의 시작 위치는 도착 위치보다 작다.

# 출력
# 세준이가 운전해야하는 거리의 최솟값을 출력하시오.

import sys, heapq
input = sys.stdin.readline
INF = int(1e9)
n, d = map(int, input().split())

graph = [[] for _ in range(d+1)]
distance = [INF] * (d + 1)

for _ in range(n) :
    start, end, dist = map(int, input().split())
    if end <= d :
        graph[start].append((end,dist))

def solution() :
    distance[0] = 0

    for i in range(d) :
        if distance[i+1] > distance[i] + 1 :
            distance[i+1] = distance[i] + 1
        for j in graph[i] :
            cost = distance[i] + j[1]
            if distance[j[0]] > cost :
                distance[j[0]] = cost

solution()

print(distance[-1])