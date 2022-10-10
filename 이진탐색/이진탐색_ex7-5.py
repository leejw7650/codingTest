from sys import stdin

n = int(stdin.readline())
shop = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
customer = list(map(int, stdin.readline().split()))

shop.sort()

def search(array, target, start, end) :
    while start <= end :
        mid = (start + end) // 2

        if array[mid] == target or array[start] == target or array[end] == target :
            return True

        elif array[mid] > target :
            end = mid - 1
        elif array[mid] < target :
            start = mid + 1

    return False

for i in customer :
    result = search(shop, i, start = 0, end = n - 1)
    if result == True :
        print('yes', end = ' ')
    else :
        print('no', end = ' ')