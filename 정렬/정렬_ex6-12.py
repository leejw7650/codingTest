import sys

n, k = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))
a.sort()
b = list(map(int, sys.stdin.readline().split()))
b.sort(reverse = True)

for i in range(k) :
    if a[i] < b[i] :
        a[i], b[i] = b[i], a[i]