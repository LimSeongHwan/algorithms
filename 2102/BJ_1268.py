def solution(n):
    student_class = []
    leader = [[0, []] for _ in range(n)]
    res = []
    
    for _ in range(n):
        student_class.append(list(map(int, input().split())))
    
    for i in range(5):
        for j in range(n-1):
            for k in range(j+1, n):
                if student_class[j][i] == student_class[k][i]:
                    if (k not in leader[j][1]):
                        leader[j][0] += 1
                        leader[k][0] += 1
                        leader[j][1].append(k)
                        leader[k][1].append(j)
                    
    for i in range(len(leader)):
        if leader[i][0] == max(leader)[0]:
            res.append(i+1)

    return min(res)

n = int(input())
print(solution(n))