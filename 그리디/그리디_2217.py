import sys

n = int(input())

rope = []

for i in range(n) :
    rope.append(int(sys.stdin.readline()))

rope.sort(reverse = True)

weight = [i*j for i,j in zip(list(range(1, n+1)), rope)]

print(max(weight))