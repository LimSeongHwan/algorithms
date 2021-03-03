def solution(num):
    res = 0

    for _ in range(num):
        word = input()
        info = dict()
        flag = True

        for idx, letter in enumerate(word):
            if letter in info:
                if info[letter] + 1 == idx:
                    info[letter] = idx
                else:
                    flag = False
                    break
            else:
                info[letter] = idx

        if flag:
            res += 1

    return res


num = int(input())
print(solution(num))