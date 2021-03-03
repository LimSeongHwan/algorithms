def solution(n, b, h, w):
    
    hotel_info = []
    min_val = 500001

    for _ in range(h):
        hotel_info.append(int(input()))
        hotel_info.append(list(map(int, input().split())))
 
    for i in range(0, len(hotel_info), 2):
        if hotel_info[i] * n <= b:
            for person in hotel_info[i+1]:
                if person >= n:
                    min_val = min(min_val, hotel_info[i] * n)

    if min_val == 500001:
        return "stay home"
    else:
        return min_val

n, b, h, w = map(int, input().split())
print(solution(n, b, h, w))