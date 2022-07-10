n, m = map(int, input().split())

ball = list(map(int, input().split()))

result = 0

for i in range(n-1) :
    for j in range(i,n) :
        if ball[i] != ball[j] :
            result += 1

print(result)