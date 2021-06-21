# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    res = []
    ans = ''
    name_dict = dict()
    names = S.split('; ')

    for name in names:
        name_split = name.split(' ')
        first_name = name_split[0]
        last_name = name_split[-1]

        if (first_name + ' ' + last_name) not in name_dict:
            name_dict[first_name + ' ' + last_name] = 1
            res.append(name + ';' + first_name.lower() + '.' + last_name.lower().replace('-', '')[:8])
        else:
            name_dict[first_name + ' ' + last_name] += 1
            res.append(name + ';' + first_name.lower() + '.' + last_name.lower().replace('-', '')[:8] + str(name_dict[first_name + ' ' + last_name]))

    for name in res:
        name_split = name.split(';')
        ori_name = name_split[0]
        email = '<' + name_split[-1] + '@' + C.lower() + '.com' + '>'
        ans += (ori_name + ' ' + email + '; ')
        
    return ans[:-2]
