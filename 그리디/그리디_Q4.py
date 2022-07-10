n = int(input())

money = list(map(int, input().split()))

money.sort()

for i in range(sum(money)):
    