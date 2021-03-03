def solution(stick_length):
    sticks = [64, 32, 16, 8, 4, 2, 1, 1]
    sum_val = 0
    count = 0
    
    if stick_length in sticks:
        return 1

    for i in range(len(sticks)):
        if (stick_length > sticks[i]) and (stick_length >= (sum_val + sticks[i])):
            sum_val += sticks[i]
            count += 1

            if sum_val == stick_length:
                return count

stick_length = int(input())
print(solution(stick_length))


    