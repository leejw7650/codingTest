def solution(food_times, k):
    answer = 0
    n_food = len(food_times)
    
    if sum(food_times) <= k :
        return -1

    for i in range(k) :
        while food_times[answer] == 0:
            answer = (answer + 1) % n_food
        food_times[answer] -= 1
        answer = (answer + 1) % n_food

    answer += 1
    return answer

a = solution([1,2,3], 7)

print(a)