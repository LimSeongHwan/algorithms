def solution(king_pos, stone_pos, n):

    def move_R(pos):
        if ord(pos[0]) + 1 <= 72:
            pos[0] = chr(ord(pos[0]) + 1)
        return pos

    def move_L(pos):
        if ord(pos[0]) - 1 >= 65:
            pos[0] = chr(ord(pos[0]) - 1)
        return pos

    def move_B(pos):
        if (pos[1] - 1) >= 1:
            pos[1] -= 1
        return pos

    def move_T(pos):
        if (pos[1] + 1) <= 8:
            pos[1] += 1
        return pos
        
    def move_RT(pos):
        if (ord(pos[0]) + 1) <= 72 and (pos[1] + 1) <= 8:
            pos[0] = chr(ord(pos[0]) + 1)
            pos[1] += 1
        return pos

    def move_LT(pos):
        if (ord(pos[0]) - 1) >= 65 and (pos[1] + 1) <= 8:
            pos[0] = chr(ord(pos[0]) - 1)
            pos[1] += 1
        return pos

    def move_RB(pos):
        if (ord(pos[0]) + 1) <= 72 and (pos[1] - 1) >= 1:
            pos[0] = chr(ord(pos[0]) + 1)
            pos[1] -= 1
        return pos

                
    def move_LB(pos):
        if (ord(pos[0]) - 1) >= 65 and (pos[1] - 1) >= 1:
            pos[0] = chr(ord(pos[0]) - 1)
            pos[1] -= 1
        return pos

    king_pos = list(king_pos)
    king_pos[1] = int(king_pos[1])
    stone_pos = list(stone_pos)
    stone_pos[1] = int(stone_pos[1])
    n = int(n)

    for _ in range(n):
        move_val = input()
        
        if move_val == 'R':
            temp_pos = king_pos[:]
            temp_pos2 = stone_pos[:]

            if move_R(temp_pos) == stone_pos:
                if move_R(temp_pos2) != stone_pos:
                    king_pos = move_R(king_pos)
                    stone_pos = move_R(stone_pos)
            else:
                king_pos = move_R(king_pos)

        elif move_val == 'L':
            temp_pos = king_pos[:]
            temp_pos2 = stone_pos[:]

            if move_L(temp_pos) == stone_pos:
                if move_L(temp_pos2) != stone_pos:
                    king_pos = move_L(king_pos)
                    stone_pos = move_L(stone_pos)
            else:
                king_pos = move_L(king_pos)

        elif move_val == 'B':
            temp_pos = king_pos[:]
            temp_pos2 = stone_pos[:]

            if move_B(temp_pos) == stone_pos:
                if move_B(temp_pos2) != stone_pos:
                    king_pos = move_B(king_pos)
                    stone_pos = move_B(stone_pos)
            else:
                king_pos = move_B(king_pos)

        elif move_val == 'T':
            temp_pos = king_pos[:]
            temp_pos2 = stone_pos[:]

            if move_T(temp_pos) == stone_pos:
                if move_T(temp_pos2) != stone_pos:
                    king_pos = move_T(king_pos)
                    stone_pos = move_T(stone_pos)
            else:
                king_pos = move_T(king_pos)

        elif move_val == 'RT':
            temp_pos = king_pos[:]
            temp_pos2 = stone_pos[:]

            if move_RT(temp_pos) == stone_pos:
                if move_RT(temp_pos2) != stone_pos:
                    king_pos = move_RT(king_pos)
                    stone_pos = move_RT(stone_pos)
            else:
                king_pos = move_RT(king_pos)

        elif move_val == 'LT':
            temp_pos = king_pos[:]
            temp_pos2 = stone_pos[:]

            if move_LT(temp_pos) == stone_pos:
                if move_LT(temp_pos2) != stone_pos:
                    king_pos = move_LT(king_pos)
                    stone_pos = move_LT(stone_pos)
            else:
                king_pos = move_LT(king_pos)

        elif move_val == 'RB':
            temp_pos = king_pos[:]
            temp_pos2 = stone_pos[:]

            if move_RB(temp_pos) == stone_pos:
                if move_RB(temp_pos2) != stone_pos:
                    king_pos = move_RB(king_pos)
                    stone_pos = move_RB(stone_pos)
            else:
                king_pos = move_RB(king_pos)

        else:
            temp_pos = king_pos[:]
            temp_pos2 = stone_pos[:]

            if move_LB(temp_pos) == stone_pos:
                if move_LB(temp_pos2) != stone_pos:
                    king_pos = move_LB(king_pos)
                    stone_pos = move_LB(stone_pos)
            else:
                king_pos = move_LB(king_pos)

    return king_pos, stone_pos

king_pos, stone_pos, n = input().split()
king_pos, stone_pos = solution(king_pos, stone_pos, n)
print(''.join(king_pos[0] + str(king_pos[1])))
print(''.join(stone_pos[0] + str(stone_pos[1])))