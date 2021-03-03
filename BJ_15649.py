num_range, num_len = map(int, input().split())
num = [i for i in range(1, num_range + 1)]
check = [False] * num_range
res = []


def solution(idx):
    if idx == num_len:
        print(" ".join(map(str, res)))
    for i in range(num_range):
        if not check[i]:
            check[i] = True
            res.append(num[i])
            solution(idx + 1)
            res.pop()
            check[i] = False


solution(0)