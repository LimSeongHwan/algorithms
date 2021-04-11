card_num, card_sum = map(int, input().split())
cards = list(map(int, input().split()))
res = [0] * card_num
ans = []
max_val = 0


def solution(idx, start, now_sum):
    global max_val

    if now_sum > card_sum:
        return
    if idx == 3:
        if now_sum > max_val:
            max_val = now_sum
    else:
        for i in range(start, card_num):
            res[idx] = cards[i]
            solution(idx + 1, i + 1, now_sum + cards[i])


solution(0, 0, 0)
print(max_val)