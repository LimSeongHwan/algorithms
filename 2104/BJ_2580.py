def find_num(y, x):
    numbers = [i + 1 for i in range(9)]
    for k in range(9):
        if area[y][k] in numbers:
            numbers.remove(area[y][k])
        if area[k][x] in numbers:
            numbers.remove(area[k][x])
    for i in range((y//3)*3, ((y//3)+1)*3):
        for j in range((x//3)*3, ((x//3)+1)*3):
            if area[i][j] in numbers:
                numbers.remove(area[i][j])
    return numbers


def solution(count):
    global flag
    if count == len(start_idx):
        flag = True
        for row in area:
            print(' '.join(map(str, row)))
        return
    else:
        y, x = start_idx[count]
        nums = find_num(y, x)
        for num in nums:
            if not flag:
                area[y][x] = num
                solution(count + 1)
                area[y][x] = 0


flag = False
area = []
start_idx = []
for i in range(9):
    info = list(map(int, input().split()))
    for j in range(9):
        if info[j] == 0:
            start_idx.append((i, j))
    area.append(info)
solution(0)