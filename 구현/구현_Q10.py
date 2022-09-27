def solution(n,m) :
    import sys
    
    lock = [[0]] * n
    key = []

    for _ in range(n) :
        lock.append([0]*n + list(map(int, sys.stdin.readline().split())) + [0]*n)
    
    lock = [[0]] * n
    
    for _ in range(m) :
        key.append(list(map(int, sys.stdin.readline().split())))

    for i in range(3*n - m) :
        for j in range(3*n - m) :
            temp = [[0] * (3*n)] * (3*n)
            for k in range(m) :
                for l in range(m) :
                    temp[i][j] = lock[i][j] + key[k][l]
            for p in range(n) :
                for q in range(n) :
                    if temp[n+p][n+q] == 1 :
                        pass
                    else :
                        