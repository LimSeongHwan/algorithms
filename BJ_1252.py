def solution(num, num2):
    num.reverse()
    num2.reverse()
    length = max(len(num), len(num2))
    plus_val = 0
    res = []

    if len(num) < length:
        for _ in range(length - len(num)):
            num.append('0')

    if len(num2) < length:
        for _ in range(length - len(num2)):
            num2.append('0')

    for i in range(length):
        sum_value = int(num[i]) + int(num2[i]) + plus_val
        plus_val = 0

        if sum_value == 2:
            res.append(0)
            plus_val = 1
        elif sum_value == 3:
            res.append(1)
            plus_val = 1
        else:
            res.append(sum_value)

    if plus_val == 1:
        res.append(1)

    res.reverse()

    while res[0] != 1 and len(res) != 1:
        res.pop(0)

    return ''.join(list(map(str, res)))

num, num2 = map(list, input().split())
print(solution(num, num2))