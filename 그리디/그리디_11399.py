n = int(input())

time = list(map(int, input().split()))

time.sort()

result = 0

for i in range(n) :
    result += sum(time[:i+1])

print(result)