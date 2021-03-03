def solution(y, x):
    areas = []
    row_area = [0] * y
    col_area = [0] * x
    row_need_guard = 0
    col_need_guard = 0
    
    for _ in range(y):
        areas.append(input())
        
    for i in range(y):
        for j in range(x):
            if areas[i][j] == 'X':
                col_area[j] = 1
                row_area[i] = 1
                
    for area in col_area:
        if area != 1:
            col_need_guard += 1
            
    for area in row_area:
        if area != 1:
            row_need_guard += 1
                
    return max(row_need_guard, col_need_guard)

y, x = map(int, input().split())
print(solution(y, x))