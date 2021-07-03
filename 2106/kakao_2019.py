import sys
sys.setrecursionlimit(10000000)


def solution(user_id, banned_id):

    def solution2(idx, arr):
        nonlocal cnt
        if idx == target:
            print(arr)
            cnt += 1
        else:
            for i in range(len(values[idx])):
                if values[idx][i] not in arr:
                    solution2(idx + 1, arr + [values[idx][i]])

    user_id = set(user_id)
    ban_dict = dict()
    ban_name_cnt = dict()
    res = []
    target = len(banned_id)
    cnt = 0

    for ban_id in banned_id:
        user_list = []
        star_idx = dict()
        for i in range(len(ban_id)):
            if ban_id[i] == '*':
                star_idx[i] = 1

        for user in user_id:
            flag = True
            if len(ban_id) == len(user):
                for i in range(len(ban_id)):
                    if ban_id[i] != user[i]:
                        if i not in star_idx:
                            flag = False
                            break

                if flag:
                    user_list.append(user)

        if ban_id not in ban_dict:
            ban_dict[ban_id] = user_list
            ban_name_cnt[ban_id] = 1
        else:
            ban_name_cnt[ban_id] += 1

    del_list = []
    for key, values in ban_dict.items():
        if ban_name_cnt[key] == len(values):
            target -= ban_name_cnt[key]
            del_list.append(key)
    for data in del_list:
        del ban_dict[data]

    values = list(ban_dict.values())

    if len(values) >= 2:
        visited = [[0] * len(value) for value in values]
        solution2(0, [])
        return cnt
    else:
        return len(values[0])


# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc", "frodo"], ["fr*d*", "abc1**"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "******", "*rodo", "******"]))
print(solution(["frodo", "fradi", "frado", "frcdo", "frbdo"], ["fr*d*", "*****"]))
