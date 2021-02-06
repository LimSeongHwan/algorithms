def solution(name):
    count_val = int(input())
    name_count_L = 0
    name_count_O = 0
    name_count_V = 0
    name_count_E = 0
    res = []
    percentage = 0

    if 'L' in name:
        name_count_L += 1

    if 'O' in name:
        name_count_O += 1

    if 'V' in name:
        name_count_V += 1

    if 'E' in name:
        name_count_E += 1

    for i in range(count_val):
            
        girl_name = input()
        girl_name_count_L = 0
        girl_name_count_O = 0
        girl_name_count_V = 0
        girl_name_count_E = 0
        
        if 'L' in girl_name:
            girl_name_count_L += 1

        if 'O' in girl_name:
            girl_name_count_O += 1

        if 'V' in girl_name:
            girl_name_count_V += 1

        if 'E' in girl_name:
            girl_name_count_E += 1 
        



    