while True:
    num = input()
    flag_val = True
    
    if num == '0':
        break
        
    for i in range(len(num)):
        if num[i] != num[(len(num)-1)-i]:
            flag_val = False
            
    if flag_val:
        print("yes")
        
    else:
        print("no")