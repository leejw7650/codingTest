n = input()

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cro :
    if i in n :
        n = n.replace(i, 'a')

print(len(n))