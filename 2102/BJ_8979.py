country, target = map(int, input().split())
countries = []
target_idx = 0
rank = 1

for i in range(country):
    input_val = list(map(int, input().split())) 
    countries.append(input_val)

    if input_val[0] == target:
        target_idx = i

for i in range(country):
    if target_idx != i:
        if countries[target_idx][1] < countries[i][1]:
            rank += 1
        elif countries[target_idx][1] == countries[i][1]:
            if countries[target_idx][2] < countries[i][2]:
                rank += 1
            elif countries[target_idx][2] == countries[i][2]:
                if countries[target_idx][3] < countries[i][3]:
                    rank += 1

print(rank)

