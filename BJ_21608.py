num = int(input())
area = [[0] * num for _ in range(num)]
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

info_dict = dict()
for _ in range(num ** 2):
    temp = list(map(int, input().split()))
    info_dict[temp[0]] = temp[1:]

for key, value in info_dict.items():
    max_like_cnt = 0
    max_blank_cnt = 0
    like_index = []
    
    for i in range(num):
        for j in range(num):
            if not area[i][j]:
                like_cnt = 0
                blank_cnt = 0
                
                for k in range(4):
                    ny = dy[k] + i
                    nx = dx[k] + j

                    if (0 <= ny < num) and (0 <= nx < num):
                        if area[ny][nx] in value:
                            like_cnt += 1
                        elif area[ny][nx] == 0:
                            blank_cnt += 1

                if like_cnt > max_like_cnt:
                    like_index = [(i, j)]
                    blank_index = (i, j)
                    max_like_cnt = like_cnt
                    max_blank_cnt = blank_cnt

                elif like_cnt == max_like_cnt:
                    like_index.append((i, j))

                    if blank_cnt >= max_blank_cnt:
                        blank_index = (i, j)
                        max_blank_cnt = blank_cnt
    
    if len(like_index) > 1:
        area[blank_index[0]][blank_index[1]] = key
    else:
        area[like_index[0][0]][like_index[0][1]] = key
        
satisfied = 0
for i in range(num):
    for j in range(num):
        cnt = 0
        for k in range(4):
            ny = dy[k] + i
            nx = dx[k] + j
            if (0 <= ny < num) and (0 <= nx < num) and (area[ny][nx] in info_dict[area[i][j]]):
                cnt += 1

        if cnt == 1:
            satisfied += 1
        elif cnt == 2:
            satisfied += 10
        elif cnt == 3:
            satisfied += 100
        elif cnt == 4:
            satisfied += 1000

print(satisfied)