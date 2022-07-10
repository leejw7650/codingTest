import sys

n = int(input())

rank = []
for i in range(n):
    rank.append(int(sys.stdin.readline()))

rank.sort()

for i in range(n) :
    rank[i] = abs(rank[i] - (i+1))

print(sum(rank))