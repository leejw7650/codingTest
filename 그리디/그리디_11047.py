n, k = map(int, input().split())

money = []

for i in range(n) :
    money.append(int(input()))

money.sort(reverse = True)

result = 0

for i in range(n) :
    result += k // money[i]
    k = k % money[i]

print(result)