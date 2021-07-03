def find_block(y_idx, x_idx, direct):
    global max_score, score, pass_y, pass_x
    score += 1

    if direct == 0:
        if y_idx != 0:
            y_idx -= 1
        while not area[y_idx][x_idx]:
            if y_idx == 0:
                direct = 1
                score += 1
                y_idx, x_idx, direct = find_block(y_idx, x_idx, direct)
                break
            if (y_idx == start_y) and (x_idx == start_x):
                if score > max_score:
                    max_score = score
                return -2, -2, -2
            y_idx -= 1

    elif direct == 1:
        if y_idx != (area_length - 1):
            y_idx += 1
        while not area[y_idx][x_idx]:
            if y_idx == (area_length - 1):
                direct = 0
                score += 1
                y_idx, x_idx, direct = find_block(y_idx, x_idx, direct)
                break
            if (y_idx == start_y) and (x_idx == start_x):
                if score > max_score:
                    max_score = score
                return -2, -2, -2
            y_idx += 1

    elif direct == 2:
        if x_idx != 0:
            x_idx -= 1
        while not area[y_idx][x_idx]:
            if x_idx == 0:
                direct = 3
                score += 1
                y_idx, x_idx, direct = find_block(y_idx, x_idx, direct)
                break
            if (y_idx == start_y) and (x_idx == start_x):
                if score > max_score:
                    max_score = score
                return -2, -2, -2
            x_idx -= 1

    else:
        if x_idx != (area_length - 1):
            x_idx += 1
        while not area[y_idx][x_idx]:
            if x_idx == (area_length - 1):
                direct = 2
                score += 1
                y_idx, x_idx, direct = find_block(y_idx, x_idx, direct)
                break
            if (y_idx == start_y) and (x_idx == start_x):
                if score > max_score:
                    max_score = score
                return -2, -2, -2
            x_idx += 1

    pass_y, pass_x = y_idx, x_idx
    return y_idx, x_idx, direct


def heat_block(y_idx, x_idx, direct):
    global max_score
    if area[y_idx][x_idx] == -1:
        if (score - 1) > max_score:
            max_score = score - 1
        return

    elif area[y_idx][x_idx] == 1:
        if direct == 0:
            y, x, direct = find_block(y_idx, x_idx, 1)
        elif direct == 1:
            y, x, direct = find_block(y_idx, x_idx, 3)
        elif direct == 2:
            y, x, direct = find_block(y_idx, x_idx, 0)
        elif direct == 3:
            y, x, direct = find_block(y_idx, x_idx, 2)

    elif area[y_idx][x_idx] == 2:
        if direct == 0:
            y, x, direct = find_block(y_idx, x_idx, 3)
        elif direct == 1:
            y, x, direct = find_block(y_idx, x_idx, 0)
        elif direct == 2:
            y, x, direct = find_block(y_idx, x_idx, 1)
        elif direct == 3:
            y, x, direct = find_block(y_idx, x_idx, 2)

    elif area[y_idx][x_idx] == 3:
        if direct == 0:
            y, x, direct = find_block(y_idx, x_idx, 2)
        elif direct == 1:
            y, x, direct = find_block(y_idx, x_idx, 0)
        elif direct == 2:
            y, x, direct = find_block(y_idx, x_idx, 3)
        elif direct == 3:
            y, x, direct = find_block(y_idx, x_idx, 1)

    elif area[y_idx][x_idx] == 4:
        if direct == 0:
            y, x, direct = find_block(y_idx, x_idx, 1)
        elif direct == 1:
            y, x, direct = find_block(y_idx, x_idx, 2)
        elif direct == 2:
            y, x, direct = find_block(y_idx, x_idx, 3)
        elif direct == 3:
            y, x, direct = find_block(y_idx, x_idx, 0)

    elif area[y_idx][x_idx] == 5:
        if direct == 0:
            y, x, direct = find_block(y_idx, x_idx, 1)
        elif direct == 1:
            y, x, direct = find_block(y_idx, x_idx, 0)
        elif direct == 2:
            y, x, direct = find_block(y_idx, x_idx, 3)
        elif direct == 3:
            y, x, direct = find_block(y_idx, x_idx, 2)

    elif area[y_idx][x_idx] in [6, 7, 8, 9, 10]:
        for idx in hole_dict[area[y_idx][x_idx]]:
            if idx != (y_idx, x_idx):
                y_idx = idx[0]
                x_idx = idx[1]
        y, x, direct = find_block(y_idx, x_idx, direct)

    if (y_idx == -2):
        return
    
    elif (pass_y == y) and (pass_x == x):
        print(start_y, start_x, y_idx, x_idx, y, x)
        return
    
    return heat_block(y, x, direct)


case = int(input())
for tc in range(1, case + 1):
    area_length = int(input())
    area = []
    start_idx = []
    max_score = 0

    for i in range(area_length):
        temp = list(map(int, input().split()))
        area.append(temp)
        hole_dict = dict()

        for j in range(6, 11):
            hole_dict[j] = []

        for j in range(area_length):
            if temp[j] in [6, 7, 8, 9, 10]:
                hole_dict[temp[j]].append((i, j))
            
            elif temp[j] == 0:
                start_idx.append((i, j))

    for start_y, start_x in start_idx:
        for i in range(4):
            score, pass_y, pass_x = 0, 0, 0
            y_idx, x_idx, direct = find_block(start_y, start_x, i)
            heat_block(y_idx, x_idx, direct)

    print(max_score)