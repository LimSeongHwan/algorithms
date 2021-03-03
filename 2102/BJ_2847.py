case = int(input())
scores = []
count = 0

for _ in range(case):
    scores.append(int(input()))

for i in range(len(scores)-2, -1, -1):
    if scores[i+1] <= scores[i]:
        while scores[i+1] <= scores[i]:
            scores[i] -= 1
            count += 1
            
print(count)