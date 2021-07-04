# 문제 설명
# 사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다. 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.

# 단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# word의 길이는 1 이상 5 이하입니다.
# word는 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어져 있습니다.
# 입출력 예
# word	result
# "AAAAE"	6
# "AAAE"	10
# "I"	1563
# "EIO"	1189
# 입출력 예 설명
# 입출력 예 #1

# 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA", "AAA", "AAAA", "AAAAA", "AAAAE", ... 와 같습니다. "AAAAE"는 사전에서 6번째 단어입니다.

# 입출력 예 #2

# "AAAE"는 "A", "AA", "AAA", "AAAA", "AAAAA", "AAAAE", "AAAAI", "AAAAO", "AAAAU"의 다음인 10번째 단어입니다.

# 입출력 예 #3

# "I"는 1563번째 단어입니다.

# 입출력 예 #4

# "EIO"는 1189번째 단어입니다.


def solution(word):
    
    
    def solution2(idx, letter):
        nonlocal sum_val
        
        if i == 4:
            if word[i] == 'A':
                sum_val += 1
            elif word[i] == 'E':
                sum_val += 2
            elif word[i] == 'I':
                sum_val += 3
            elif word[i] == 'O':
                sum_val += 4
            else:
                sum_val += 5
        elif i == 3:
            if word[i] == 'A':
                sum_val += 1
            elif word[i] == 'E':
                sum_val += 7
            elif word[i] == 'I':
                sum_val += 13
            elif word[i] == 'O':
                sum_val += 19
            else:
                sum_val += 25
        elif i == 2:
            if word[i] == 'A':
                sum_val += 1
            elif word[i] == 'E':
                sum_val += 32
            elif word[i] == 'I':
                sum_val += 63
            elif word[i] == 'O':
                sum_val += 94
            else:
                sum_val += 125
        elif i == 1:
            if word[i] == 'A':
                sum_val += 1
            elif word[i] == 'E':
                sum_val += 157
            elif word[i] == 'I':
                sum_val += 313
            elif word[i] == 'O':
                sum_val += 469
            else:
                sum_val += 625
        else:
            if word[i] == 'A':
                sum_val += 1
            elif word[i] == 'E':
                sum_val += 782
            elif word[i] == 'I':
                sum_val += 1563
            elif word[i] == 'O':
                sum_val += 2344
            else:
                sum_val += 3125
                

    sum_val = 0
    for i in range(len(word)):
        solution2(i, word[i])
    return sum_val
        

A = 1
E = 2, 7, 32, 157, 782
I = 3, 13, 63, 313, 1563
O = 4, 19, 94, 469, 2344
U = 5, 25, 125, 625, 3125