def solution(idx, start):
    if idx == target:
        print(" ".join(map(str, select_num)))
    else:
        for i in range(start, num_length):
            select_num[idx] = info[i]
            solution(idx + 1, i + 1)


target = 6
info = list(map(int, input().split()))
while True:
    num_length = info.pop(0)
    select_num = [0] * target
    solution(0, 0)
    info = list(map(int, input().split()))
    if info[0] == 0:
        break
    else:
        print()