def solution(numbers, hand):

    def find_pos(number):
        for i in range(len(phone_pos)):
                for j in range(len(phone_pos[i])):
                    if phone_pos[i][j] == number:
                        return i, j
    
    answer = ''
    l_select = [1, 4, 7]
    r_select = [3, 6, 9]
    phone_pos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    l_pos = [3, 0]
    r_pos = [3, 2]
    num_pos = [0, 0]
    l_num_distance = 0
    r_num_distance = 0
    
    for num in numbers:
        if num in l_select:
            answer += 'L'
            l_pos[0], l_pos[1] = find_pos(num)
            
        elif num in r_select:
            answer += 'R'
            r_pos[0], r_pos[1] = find_pos(num)
            
        else:
            num_pos[0], num_pos[1] = find_pos(num)
            l_num_distance = abs(num_pos[0] - l_pos[0]) + abs(num_pos[1] - l_pos[1])
            r_num_distance = abs(num_pos[0] - r_pos[0]) + abs(num_pos[1] - r_pos[1])
                        
            if l_num_distance < r_num_distance:
                answer += 'L'
                l_pos = num_pos[:]

            elif l_num_distance > r_num_distance:
                answer += 'R'
                r_pos = num_pos[:]

            else:
                if hand == 'left':
                    answer += 'L'
                    l_pos = num_pos[:]

                else:
                    answer += 'R'
                    r_pos = num_pos[:]
                                
    return answer