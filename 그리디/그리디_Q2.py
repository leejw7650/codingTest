number = input()

n = len(number)

result = 0

for i in range(n) :
    result = max(result * int(number[i]), result + int(number[i]))

print(result)