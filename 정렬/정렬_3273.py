# 문제
# n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수열의 크기 n이 주어진다. 다음 줄에는 수열에 포함되는 수가 주어진다. 셋째 줄에는 x가 주어진다. (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)

# 출력
# 문제의 조건을 만족하는 쌍의 개수를 출력한다.

from sys import stdin

n = int(stdin.readline())

array = list(map(int, stdin.readline().split()))
count = [0 for _ in range(max(array) + 1)]
x = int(stdin.readline())

array.sort()
for i in array :
    count[i] = 1

def sol() :
    result = 0
    maxi = array[-1]
    mini = array[0]

    if x >= 2*maxi or x <= 2*mini or len(array)==1 :
        return result

    elif x > maxi :
        for i in range((2*maxi-x+1)//2) :
            if count[maxi - i] == count[x - maxi + i] == 1 :
                result += 1
    elif x <= maxi :
        for i in range(1, (x-1) // 2 + 1) :
            if count[x-i] == count[i] == 1 :
                result += 1
                
    return result

print(sol())