score = 0
target = 100
for i in range(10):
    item = int(input())
    
    if score + item <= target:
        score += item
    else:
        if (score + item - target) <= (target - score):
            score += item

        print(score)
        break

    if i == 9:
        print(score)