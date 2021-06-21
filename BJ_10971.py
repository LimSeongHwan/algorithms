def solution(idx, sum_val, end):
    global min_val

    if sum_val > min_val:
        return

    if idx == (city_num - 1):
        if area[end][start]:
            sum_val += area[end][start]
            if sum_val < min_val:
                min_val = sum_val
        else:
            return
    
    else:
        for i in range(city_num):
            if (not city_check[i]) and area[end][i]:
                city_check[i] = 1
                solution(idx + 1, sum_val + area[end][i], i)
                city_check[i] = 0

city_num = int(input())
area = [list(map(int, input().split())) for _ in range(city_num)]
min_val = 0xffffff
for i in range(city_num):
    city_check = [0] * city_num
    city_check[i] = 1
    start = i
    solution(0, 0, i)
print(min_val)