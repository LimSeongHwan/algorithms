def solution(n, m):
    chess_area = []
    min_val = 9999

    for _ in range(n):
        chess_area.append(input())

    for i in range(n-7):
        for j in range(m-7):
            count1 = 0
            count2 = 0

            for k in range(i, i+8): 
                for l in range(j, j+8):
                    if (not (k % 2)):
                        if (not (l % 2)) and chess_area[k][l] != 'B':
                            count1 += 1
                        elif (l % 2) and chess_area[k][l] != 'W':
                            count1 += 1
                    else:
                        if (not (l % 2)) and chess_area[k][l] != 'W':
                            count1 += 1
                        elif (l % 2) and chess_area[k][l] != 'B':
                            count1 += 1
                    if (not (k % 2)):
                        if (not (l % 2)) and chess_area[k][l] != 'W':
                            count2 += 1
                        elif (l % 2) and chess_area[k][l] != 'B':
                            count2 += 1
                    else:
                        if (not (l % 2)) and chess_area[k][l] != 'B':
                            count2 += 1
                        elif (l % 2) and chess_area[k][l] != 'W':
                            count2 += 1

            min_val = min(min_val, count1, count2)
            
    return min_val

n, m = map(int, input().split())
print(solution(n, m))