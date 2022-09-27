num = [i+1 for i in range(10000)]

def sol(n, num) :
    tmp = sum(map(int, list(str(n))))
    n += tmp
    if n in num :
        num.remove(n)
        sol(n, num)
    else :
        pass


for i in num :
    sol(i, num)
    print(i)