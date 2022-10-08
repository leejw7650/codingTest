import sys

n = int(sys.stdin.readline())

student = []
for i in range(n) :
    name, score = sys.stdin.readline().split()
    student.append([name, int(score)])

student.sort(key = lambda x:(x[1]))

for i in student :
    print(i[0], end = ' ')