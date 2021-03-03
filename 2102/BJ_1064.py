from decimal import *


def solution(points):

    getcontext().prec = 16

    point_1 = list(points[0:2])
    point_2 = list(points[2:4])
    point_3 = list(points[4:6])

    if (point_2[1] - point_1[1]) * (point_3[0] - point_1[0]) == (
        point_2[0] - point_1[0]
    ) * (point_3[1] - point_1[1]):
        return -1

    long_val = max(
        (point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2,
        (point_1[0] - point_3[0]) ** 2 + (point_1[1] - point_3[1]) ** 2,
        (point_2[0] - point_3[0]) ** 2 + (point_2[1] - point_3[1]) ** 2,
    )

    short_val = min(
        (point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2,
        (point_1[0] - point_3[0]) ** 2 + (point_1[1] - point_3[1]) ** 2,
        (point_2[0] - point_3[0]) ** 2 + (point_2[1] - point_3[1]) ** 2,
    )

    return (long_val ** (1 / 2) - short_val ** (1 / 2)) * 2


points = list(map(int, input().split()))
print(solution(points))