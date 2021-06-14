N = int(input())
order = []
likes = [[] for _ in range(N * N)]
for i in range(N * N):
    A, B, C, D, E = map(int, input().split())
    order.append(A - 1)
    likes[A - 1].append(B-1)
    likes[A - 1].append(C-1)
    likes[A - 1].append(D-1)
    likes[A - 1].append(E-1)

place = [[-1] * N for _ in range(N)]    # 비어있는 자리 -1
# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for student in order:   # 순서대로 학생을 정렬할거임
    # max값 초기화
    max_cnt = -1
    max_zero_cnt = -1
    tmp_zero_cnt = -1
    position_r = -1
    position_c = -1
    first_position_r = -1
    first_position_c = -1
    for r in range(N):
        for c in range(N):
            cnt = 0         # 사방에 좋아하는 친구가 있는지 카운트 변수
            zero_cnt = 0    # 사방에 좋아하는 친구가 없을 때 이용, 좋아하는 친구가 없는 곳 카운트
            if place[r][c] == -1:   # 비어있는 곳만 확인
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if (0 <= nr < N) and (0 <= nc < N):
                        if place[nr][nc] in likes[student]:     # 사방에 위치한 자리에 좋아하는 친구가 있는지
                            cnt += 1    # 있으면 카운트
                        if place[nr][nc] == -1:
                            zero_cnt += 1
                if cnt == 0:    # 사방에 좋아하는 친구가 없다면 첫 위치는 여기 !
                    if max_zero_cnt < zero_cnt:
                        max_zero_cnt = zero_cnt
                        first_position_r = r
                        first_position_c = c

                else:           # 좋아하는 친구가 있다면
                    if max_cnt < cnt:
                        max_cnt = cnt
                        position_r = r
                        position_c = c
                        tmp_zero_cnt = zero_cnt

                    elif max_cnt == cnt:    # 좋아하는 친구의 수가 같은 경우 빈자리가 많은 곳에 위치하도록 한다.
                        if tmp_zero_cnt < zero_cnt:
                            tmp_zero_cnt = zero_cnt
                            position_r = r
                            position_c = c
    if position_r == -1:    # 좋아하는 친구가 없는 경우
        place[first_position_r][first_position_c] = student
    else:                   # 좋아하는 친구가 있는 경우
        place[position_r][position_c] = student

point = 0
for r in range(N):
    for c in range(N):
        like_cnt = 0
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if place[nr][nc] in likes[place[r][c]]:
                    like_cnt += 1
        if like_cnt == 1:
            point += 1
        elif like_cnt == 2:
            point += 10
        elif like_cnt == 3:
            point += 100
        elif like_cnt == 4:
            point += 1000

print(point)