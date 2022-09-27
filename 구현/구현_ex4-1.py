n = int(input())

x, y = 1, 1

plans = input().split()

for i in plans :
    if i == 'R' :
        if y < n :
            y += 1
    elif i == 'L' :
        if y > 1 :
            y -= 1
    elif i == 'U' :
        if x < 1 :
            x -= 1
    elif i == 'D' :
        if x < n :
            x += 1
            
print(x, y)