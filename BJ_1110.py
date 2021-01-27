def solution(num):
    if num < 10:
        num = str(num) + str(0)
    
    else:
        num = str(num)
        
    cycle_val = 0
    new_num = ""
    temp_num = num[:]
    
    while new_num != num:
        sum_num = int(temp_num[0]) + int(temp_num[1])
        new_num = temp_num[-1] + str(int(temp_num[0]) + int(temp_num[1]))[-1]
        cycle_val += 1
        temp_num = new_num[:]
        
    return cycle_val
    
num = int(input())
print(solution(num))