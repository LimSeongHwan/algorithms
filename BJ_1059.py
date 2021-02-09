def solution(n):

    numbers = list(map(int, input().split()))
    numbers.sort()
    target = int(input())
    idx = 0
    res = []

    for i in range(len(numbers)):
        if numbers[i] == target:
            return 0
        elif numbers[i] > target:
            idx = i
            break
        
    if idx == 0:
        for i in range(1, numbers[idx]):
            for j in range(i, numbers[idx]):
                if (target >= i) and (target <= j) and i != j:
                    res.append([i, j])

        return len(res)

    for i in range(numbers[idx-1] + 1, numbers[idx]):
        for j in range(i, numbers[idx]):
            if (target >= i) and (target <= j) and i != j:
                res.append([i, j])

    return len(res)

n = int(input())
print(solution(n))