from time import time

n, m = map(int, input().split())

data = [[]] * n

for i in range(n):
    data[i] = list(map(int, input().split()))

start = time()

result = 0

for i in range(n):
    if min(data[i]) > result :
        result = min(data[i])

print(result)