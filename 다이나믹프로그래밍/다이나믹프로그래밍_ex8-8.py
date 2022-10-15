from sys import stdin

inf = 10001

n, m = map(int, stdin.readline().split())

array = []
for _ in range(n) :
    array.append(int(stdin.readline()))

dp = [0] + [inf] * m

for i in range(n) :
    for j in range(array[i], m + 1) :
        if dp[j - array[i]] != inf :
            dp[j] = min(dp[j], dp[j-array[i]] + 1)

if dp[m] == inf :
    print(-1)
else :
    print(dp[m])