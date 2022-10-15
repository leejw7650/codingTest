from sys import stdin

n = int(stdin.readline())

array = list(map(int, stdin.readline().split()))

dp = [0] * n

dp[0] = array[0]
dp[1] = max(array[0], array[1])

for i in range(2,n) :
    dp[i] = max(dp[i-2]+array[i], dp[i-1])

print(dp[-1])