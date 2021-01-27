def solution(n):
    
    names = []
    res = []

    for _ in range(n):
        names.append(input())
        
    common_letter = list(names[0])

    for i in range(1, n):
        
        for j in range(len(common_letter)):
            
            if names[i][j] != common_letter[j]:
                
                for k in range(j, len(common_letter)):
                    common_letter[k] = "?"

    return ''.join(common_letter)

input_val = int(input())
print(solution(input_val))