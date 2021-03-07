def solution(idx, start, now_sum):
    if now_sum > 100:
        return
    if idx == 7:
        if sum(select_height) == 100:
            select_height.sort()
            print("\n".join(map(str, select_height[2:])))
    else:
        for i in range(start, 9):
            select_height[idx] = heights[i]
            solution(idx + 1, i + 1, now_sum + heights[i])


heights = [int(input()) for _ in range(9)]
select_height = [0] * 9
solution(0, 0, 0)