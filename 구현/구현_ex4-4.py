n, m = map(int, input().split())
x, y, face = map(int, input().split())

field = []

for i in range(m) :
    line = [int(j) for j in input().split()]
    field.append(line)

exp = 1

while 1 :
    field[x][y] = 1
    if face == 0 :
        if field[x][y-1] == 0 :
            face = 3
            y -= 1
            exp += 1
        elif field[x+1][y] == 0 :
            face = 2
            x += 1
            exp += 1
        elif field[x][y+1] == 0 :
            face = 1
            y += 1
            exp += 1
        elif field[x-1][y] == 0 :
            face = 0
            x -= 1
            exp += 1
        else :
            break
        print(x,y, face)
        
    elif face == 1 :
        if field[x-1][y] == 0 :
            face = 0
            x -= 1
            exp += 1
        elif field[x][y-1] == 0 :
            face = 3
            y -= 1
            exp += 1
        elif field[x+1][y] == 0 :
            face = 2
            x += 1
            exp += 1
        elif field[x][y+1] == 0 :
            face = 1
            y += 1
            exp += 1
        else :
            break
        print(x,y, face)
    elif face == 2 :
        if field[x][y+1] == 0 :
            face = 1
            y += 1
            exp += 1
        elif field[x-1][y] == 0 :
            face = 0
            x -= 1
            exp += 1
        elif field[x][y-1] == 0 :
            face = 3
            y -= 1
            exp += 1
        elif field[x+1][y] == 0 :
            face = 2
            x += 1
            exp += 1
        else :
            break
        print(x,y, face)
    elif face == 3 :
        if field[x+1][y] == 0 :
            face = 2
            x += 1
            exp += 1
        elif field[x][y+1] == 0 :
            face = 1
            y += 1
            exp += 1
        elif field[x-1][y] == 0 :
            face = 0
            x -= 1
            exp += 1
        elif field[x][y-1] == 0 :
            face = 3
            y -= 1
            exp += 1
        else :
            break
        print(x,y, face)

print(exp)