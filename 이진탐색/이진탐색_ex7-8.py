from sys import stdin

n, m = map(int, stdin.readline().split())

array = list(map(int, stdin.readline().split()))

array.sort(reverse = True)

start = 0
end = max(array)

result = 0

while start <= end :
    print(start, end)
    mid = (start + end) // 2
    total = 0
    for i in array :
        if i > mid :
            total += i - mid

    if total < m :
        end = mid - 1

    else :
        result = mid
        start = mid + 1


print(result)