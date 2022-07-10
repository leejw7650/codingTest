n, k = map(int, input().split())

number = 0

while n != 1 :
    if n % k == 0 :
        n /= k
        number += 1
    else :
        n -= 1
        number += 1
        
print(number)