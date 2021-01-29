# 가로 비교
def solution(n):
    names = []
    res = []

    for _ in range(n):
        names.append(input())
        
    common_letter = list(names[0])

    for i in range(1, n):
        for j in range(len(common_letter)):
            if names[i][j] != common_letter[j]:
                common_letter[j] = '?'
                
    return ''.join(common_letter)

input_val = int(input())
print(solution(input_val))

# 세로 비교
def solution(n):    
    words = []
    res = ""
    same_flag = True
    
    for _ in range(n):
        words.append(list(input()))
        
    for i in range(len(words[0])):
        for j in range(1, len(words)):
            if words[j-1][i] != words[j][i]:
                same_flag = False
                res += '?'
                break
            
            same_flag = True
            
        if same_flag:    
            res += words[0][i]
                
    return res

n = int(input())
print(solution(n))