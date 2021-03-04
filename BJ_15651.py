num_range, num_length = map(int, input().split())
res = [0] * num_length


def solution(idx):
    if idx == num_length:
        for i in range(num_length):
            print(res[i], end=" ")
        print()
        return

    for i in range(num_range):
        res[idx] = i + 1
        solution(idx + 1)


solution(0)