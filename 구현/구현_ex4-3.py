location = input()

dx = ['a','b','c','d','e','f','g','h']


x = dx.index(location[0])
y = int(location[1])-1

move = [[1,-2],[1,2],[-1,-2],[-1,2],[2,-1],[2,1],[-2,-1],[-2,1]]

possible = []
for i in move :
    possible.append([x+i[0], y+i[1]])

n = len(possible)

for i in possible :
    if i[0] < 0 or i[0] > 7 or i[1] < 0 or i[1] > 7:
        n -= 1

print(n)