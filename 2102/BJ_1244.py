switch_num = int(input())
switch_status = list(map(int, input().split()))
student_num = int(input())
students = []

for _ in range(student_num):
    students.append(list(map(int, input().split())))

for i in range(student_num):
    if students[i][0] == 1:
        for j in range(students[i][1] - 1, switch_num, students[i][1]):
            if switch_status[j]:
                switch_status[j] = 0
            else:
                switch_status[j] = 1
    else:
        if switch_status[students[i][1] - 1]:
            switch_status[students[i][1] - 1] = 0
        else:
            switch_status[students[i][1] - 1] = 1

        for j in range(switch_num // 2):
            if (students[i][1] - 1 - j >= 0) and (
                (students[i][1] - 1 + j) <= (switch_num - 1)
            ):
                if (
                    switch_status[students[i][1] - 1 - j]
                    == switch_status[students[i][1] - 1 + j]
                ):
                    if switch_status[students[i][1] - 1 - j]:
                        switch_status[students[i][1] - 1 - j] = 0
                    else:
                        switch_status[students[i][1] - 1 - j] = 1
                    if switch_status[students[i][1] - 1 + j]:
                        switch_status[students[i][1] - 1 + j] = 0
                    else:
                        switch_status[students[i][1] - 1 + j] = 1
                else:
                    break

if switch_num > 20:
    if switch_num % 20:
        for i in range((switch_num // 20) + 1):
            print(" ".join(map(str, switch_status[(i * 20) : ((i * 20) + 20)])))
    else:
        for i in range(switch_num // 20):
            print(" ".join(map(str, switch_status[(i * 20) : ((i * 20) + 20)])))
else:
    print(" ".join(map(str, switch_status)))
