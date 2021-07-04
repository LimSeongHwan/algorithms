num = int(input())
tastes = [list(map(int, input().split())) for _ in range(num)]
min_val = 1000000001

def solution(idx, sour, bitter):
    global min_val

    if (idx == num):
        if bitter:
            if abs(sour - bitter) < min_val:
                min_val = abs(sour - bitter)
        return
    else:
        solution(idx + 1, sour * tastes[idx][0], bitter + tastes[idx][1])
        solution(idx + 1, sour, bitter)

solution(0, 1, 0)
print(min_val)