def solution(numbers):
    min_num = min(numbers)
    
    while True:
        cnt = 0

        for num in numbers:
            if (min_num % num) == 0:
                cnt += 1

                if cnt == 3:
                    return min_num
        min_num += 1

numbers = list(map(int, input().split()))
print(solution(numbers))