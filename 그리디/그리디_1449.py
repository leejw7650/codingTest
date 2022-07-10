n, l = map(int, input().split())

tape = 0
water = list(map(int, input().split()))
location = [0] * (max(water) + 1)
for i in water :
    location[i] = 1

for i in range(len(location)) :
    if location[i] == 1 :
        tape += 1
        location[i:(i+l)] = [0] * l

print(tape)