a, b = list(map(int, input().split()))

def solution(a, b) :
    iter = 1
    
    while a < b :
        if b % 10 == 1 :
            b = (b - 1) // 10
            iter += 1
        elif b % 2 == 0 :
            b /= 2
            iter += 1
        else :
            return -1


    if a == b :
        return iter
    else :
        return -1

print(solution(a,b))