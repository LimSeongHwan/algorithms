def solution(idx, start, now):
    if idx == 2:
        res.append(now)
    else:
        for i in range(start, area_length):
            solution(idx + 1, i + 1, now + [nums[i]])

case = int(input())
for tc in range(1, case + 1):
    area_length = int(input())
    area = [list(map(int, input().split())) for _ in range(area_length)]
    nums = [i for i in range(area_length)]
    res = []
    solution(0, 0, [])
    visited = [0] * len(res)
    min_flavor_diff = 0xffffff

    for i in range(len(res)):
        other_ingre = []
        pick_ingre = res[i]
        visited[i] = 1
        pick_flavor_sum = area[res[i][0]][res[i][1]] + area[res[i][1]][res[i][0]]
        
        for j in range(len(res)):
            if (not visited[j]) and (pick_ingre[0] not in res[j]) and (pick_ingre[1] not in res[j]):
                other_ingre.append(res[j])
        
        for j in range(len(other_ingre)):
            flavor_sum = area[other_ingre[j][0]][other_ingre[j][1]] + area[other_ingre[j][1]][other_ingre[j][0]]
            print(pick_ingre, pick_flavor_sum, area[res[i][0]][res[i][1]], area[res[i][1]][res[i][0]])
            print(other_ingre[j], flavor_sum, area[other_ingre[j][0]][other_ingre[j][1]], area[other_ingre[j][1]][other_ingre[j][0]])
            print(abs(pick_flavor_sum - flavor_sum))
            min_flavor_diff = min(abs(pick_flavor_sum - flavor_sum), min_flavor_diff)

    print('#{} {}'.format(tc, min_flavor_diff))