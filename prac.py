def solution(orders, course):
    
    def solve(idx, start, now, num):
        if idx == num:
            res.append(now)
        else:
            for i in range(start, len(order)):
                solve(idx + 1, i + 1, now + order[i], num)

    res = []
    res2 = []
    order_menu = dict()
    
    for num in course:   # ABCDE 2, 3, 4
        for order in orders:
            solve(0, 0, '', num)
    
    for menu in res:
        if menu in order_menu:
            order_menu[menu] += 1
        else:
            order_menu[menu] = 1
            
    order_menu_list = sorted(order_menu, key = lambda x:order_menu[x], reverse = True)
    
    for num in course:
        for i in range(len(order_menu_list)):
            if len(order_menu_list[i]) == num:
                res2.append(order_menu_list[i])
                if i < len(order_menu_list) - 1:
                    if (len(order_menu_list[i + 1]) == num) and (order_menu[order_menu_list[i]] == order_menu[order_menu_list[i + 1]]):
                        res2.append(order_menu_list[i + 1])
                    break
    print(res2)