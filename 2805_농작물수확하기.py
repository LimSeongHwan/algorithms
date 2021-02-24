case = int(input())
for i in range(1, case + 1):
    farm_length = int(input())
    farm_area = []
    medium = farm_length // 2
    revenue = 0

    for j in range(farm_length):
        farm_area.append(list(map(int, input())))

    for j in range(farm_length):
        if j <= medium:
            for k in range(medium - j, medium + j + 1):
                
                revenue += farm_area[j][k]
        else:
            for k in range(j + medium - farm_length + 1, (farm_length - j + medium)):
                revenue += farm_area[j][k]

    print('#{} {}'.format(i, revenue))