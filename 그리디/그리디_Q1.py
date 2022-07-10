n = int(input())

fear = list(map(int, input().split()))

fear.sort()

group = []
number = 0
for i in range(n) :
    group.append(fear[i])
    if len(group) == max(group) :
        number += 1
        group = []

print(number)