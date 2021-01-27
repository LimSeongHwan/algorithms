def solution(word):
    
    count_dict = dict()
    word = word.upper()
    max_count_key = []
    
    for alpha in word:
        if alpha in count_dict:
            count_dict[alpha] += 1
            
        else:
            count_dict[alpha] = 1
        
    for key, value in count_dict.items():
                
        if value == max(count_dict.values()):
            max_count_key.append(key)
            
    if len(max_count_key) > 1:
        return '?'
    
    else:
        return max_count_key[0]

word = input()
print(solution(word))