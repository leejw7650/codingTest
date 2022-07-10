import sys

t = int(sys.stdin.readline())

def solution() :
    n = []
    m = int(sys.stdin.readline())
    
    for j in range(m):
        n.append(list(map(int, sys.stdin.readline().split())))    
    n.sort()

    dp = [1] * m
    for i in range(m) :
        for j in range(i) :
            if n[i][1] < n[j][1] :
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

result = []

for i in range(t) :
    result.append(solution())

for i in range(t) :
    print(result[i])