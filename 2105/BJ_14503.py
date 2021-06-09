import sys 
sys.setrecursionlimit(1010)

def dfs(y, x, direct, turn_cnt):
    global clean
    
    if turn_cnt == 4:
        if direct == 0 and (area[y + 1][x] == 2):
            dfs(y + 1, x, direct, 0)
        elif direct == 1 and (area[y][x - 1] == 2):
            dfs(y, x - 1, direct, 0)
        elif direct == 2 and (area[y - 1][x] == 2):
            dfs(y - 1, x, direct, 0)
        elif direct == 3 and (area[y][x + 1] == 2):
            dfs(y, x + 1, direct, 0)
        else:
            return

    elif direct == 0:
        if not area[y][x - 1]:
            area[y][x - 1] = 2
            clean += 1
            dfs(y, x - 1, 3, 0)
        else:
            dfs(y, x, 3, turn_cnt + 1)

    elif direct == 1:
        if not area[y - 1][x]:
            area[y - 1][x] = 2
            clean += 1
            dfs(y - 1, x, 0, 0)
        else:
            dfs(y, x, 0, turn_cnt + 1)
        
    elif direct == 2:
        if not area[y][x + 1]:
            area[y][x + 1] = 2
            clean += 1
            dfs(y, x + 1, 1, 0)
        else:
            dfs(y, x, 1, turn_cnt + 1)

    elif direct == 3: 
        if not area[y + 1][x]:
            area[y + 1][x] = 2
            clean += 1
            dfs(y + 1, x, 2, 0)
        else:
            dfs(y, x, 2, turn_cnt + 1)

row, col = map(int, input().split())
robot_y, robot_x, direct = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(row)]
clean = 1
area[robot_y][robot_x] = 2
dfs(robot_y, robot_x, direct, 0)
print(clean)