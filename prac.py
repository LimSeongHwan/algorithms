for tc in range(int(input())):
    player = [0] * 11
    for i in range(11):
        player[i] = list(map(int, input().split()))
    visit = [0] * 11
    max_val = 0
    res = [0] * 11

    def comb(index=0):
        if index == 11:
            print(res)
        else:
            for i in range(11):
                if not player[i][index] or visit[i] == 1:
                    continue
                visit[i] = 1
                res[index] = player[i][index]
                comb(index + 1)
                visit[i] = 0

    comb()
    print(max_val)