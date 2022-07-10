import sys

n = int(input())

conf = []

time = [[0,0]]

for i in range(n) :
    conf.append(list(map(int, sys.stdin.readline().split())))

conf.sort()

for i in range(n) :
    end = time[-1][1]
    if end > conf[i][1] :
        time[-1] = conf[i]
    elif time[-1][1] <= conf[i][0] :
        time.append(conf[i])

print(len(time) - 1)