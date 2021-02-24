case = int(input())

for i in range(1, case+1):
    area = []

    for j in range(9):
        area.append(list(map(int, input().split())))

    for j in range(9):
        nums_horison = []
        nums_vertical = []
        res = 1

        for k in range(9):
            if area[j][k] not in nums_horison:
                nums_horison.append(area[j][k])
            else:
                res = 0
                break

            if area[k][j] not in nums_vertical:
                nums_vertical.append(area[k][j])
            else:
                res = 0
                break

            if ((j % 3) == 0) and ((k % 3) == 0):
                nums_square = []

                for l in range(3):
                    for m in range(3):
                        if area[j+l][k+m] not in nums_square:
                            nums_square.append(area[j+l][k+m])
                        else:
                            res = 0
                            break

        if (not res):
            break

    print('#{} {}'.format(i, res))