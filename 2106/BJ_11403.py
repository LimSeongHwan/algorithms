import sys

area_length = int(input())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(area_length)]

for k in range(area_length):
    for i in range(area_length):
        for j in range(area_length):
            if (not area[i][j]) and ((area[i][k] == 1) and (area[k][j] == 1)):
                area[i][j] = 1

for data in area:
    print(' '.join(map(str, data)))


# def dfs(now, cnt):
#     if cnt == (area_length + 1):
#         return
#     if start == now:
#         area[start][now] = 1
#         return
#     for i in range(area_length):
#         if area[now][i]:
#             area[start][i] = 1
#             dfs(now, cnt + 1)
        
# for i in range(area_length):
#     start = i
#     for j in range(area_length):
#         if area[start][j]:
#             dfs(j, 0)

# for i in range(area_length):
#     for j in range(area_length):
#         if not area[i][j]:
#             start = i
#             for k in range(area_length):
#                 if area[start][k]:
#                     dfs(k, 0)
# print(area)