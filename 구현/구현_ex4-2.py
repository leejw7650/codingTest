n = int(input())

min = sec = 5 * 9

hour = len([i for i in range(n+1) if i != 3])


N = (n+1)*60*60 - hour * min * sec

print(N)