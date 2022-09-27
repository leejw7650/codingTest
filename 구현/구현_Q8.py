s = list(input())

alphabet = []
integer = []

for i in s :
    if i.isnumeric() :
        integer.append(int(i))
    else :
        alphabet.append(i)

alphabet.sort()

print(''.join(alphabet) + str(sum(integer)))