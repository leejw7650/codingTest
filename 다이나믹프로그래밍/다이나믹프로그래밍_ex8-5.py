n = int(input())

inf = 1000001
array = [inf] * (n+1)
array[1] = 0

for i in range(1, n+1) :
    if i+1 <= n :
        array[i+1] = min(array[i+1], array[i] + 1)
    if 5*i <= n :
        array[5*1] = min(array[5*i], array[i] + 1)
    if 3*i <= n :
        array[3*i] = min(array[3*i], array[i] + 1)
    if 2*i <= n :
        array[2*i] = min(array[2*i], array[i] + 1)

print(array[n])