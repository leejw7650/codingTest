# 문제
# 지민이는 세계에서 가장 유명한 사람이 누구인지 궁금해졌다. 가장 유명한 사람을 구하는 방법은 각 사람의 2-친구를 구하면 된다. 어떤 사람 A가 또다른 사람 B의 2-친구가 되기 위해선, 두 사람이 친구이거나, A와 친구이고, B와 친구인 C가 존재해야 된다. 여기서 가장 유명한 사람은 2-친구의 수가 가장 많은 사람이다. 가장 유명한 사람의 2-친구의 수를 출력하는 프로그램을 작성하시오.

# A와 B가 친구면, B와 A도 친구이고, A와 A는 친구가 아니다.

# 입력
# 첫째 줄에 사람의 수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 각 사람이 친구이면 Y, 아니면 N이 주어진다.

# 출력
# 첫째 줄에 가장 유명한 사람의 2-친구의 수를 출력한다.

import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
graph = [[] for _ in range(n)]

for i in range(n) :
    array = list(input().rstrip())
    for j in range(n):
        if array[j] == 'Y' :
            graph[i].append(1)
        else :
            graph[i].append(0)

for i in range(n) :
    for j in range(i+1,n) :
        if graph[i][j] == 0 :
            for k in range(n) :
                if graph[i][k] == graph[k][j] == 1 :
                    graph[i][j] = 2
                    graph[j][i] = 2
                    break

result = []
for i in range(n) :
    result.append(n - graph[i].count(0))

print(max(result))