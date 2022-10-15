# 문제
# 45656이란 수를 보자.

# 이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

# N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.

# 입력
# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

n = int(input())

def sol(n, array, turn) :
    x = array[turn]
    if x % 10 == 0 :
        array.append(x*10 + 1)
    elif x % 10 == 9 :
        array.append(x*10 + 8)
    else :
        array.append(x*10 + x%10 - 1)
        array.append(x*10 + x%10 + 1)

count = 0
array = list(range(1,10))
turn = 0

while True :
    sol(n, array, turn)
    if len(str(array[turn])) == n :
        count += 1
    elif len(str(array[turn])) == n + 1 :
        print(count)
        break
    turn += 1
    
    