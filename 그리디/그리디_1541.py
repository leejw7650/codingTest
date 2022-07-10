equation = input()

n = len(equation)
result = '('

symbol = 1

for i in range(n) :
    if equation[i] == '-' :
        result += ')-('
        symbol = 1
    elif equation[i] == '+' :
        result += '+'
        symbol = 1
    elif symbol == 1 and equation[i] == '0':
        pass
    else :
        result += equation[i]
        symbol = 0
result += ')'

print(eval(result))