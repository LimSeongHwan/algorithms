pass_length, key_length = map(int, input().split())
pass_keys = sorted(input().split())
res = [0] * pass_length
vowel = "aeiou"
count_vowel = 0
count_cons = 0


def solution(idx, start, count_vowel, count_cons):
    if (count_vowel >= pass_length - 1) or (count_cons >= pass_length):
        return

    if idx == pass_length:
        print("".join(res))

    else:
        for i in range(start, key_length):
            res[idx] = pass_keys[i]
            if pass_keys[i] in vowel:
                solution(idx + 1, i + 1, count_vowel + 1, count_cons)
            else:
                solution(idx + 1, i + 1, count_vowel, count_cons + 1)


solution(0, 0, count_vowel, count_cons)