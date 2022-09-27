import sys

k = int(input())

money = []

for _ in range(k) :
    n = int(sys.stdin.readline())
    if n == 0 :
        money.pop()
    else :
        money.append(n)

print(sum(money))