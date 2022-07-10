n = int(input())

def solution(n) :
    max = n // 5
    for i in reversed(range(max+1)) :
        a = n - 5*i
        if a % 3 == 0:
            return i + a / 3
    return -1

print(int(solution(n)))