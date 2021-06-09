def solution(idx, res, course):
    global min_val, max_val

    if idx == len(oper):
        print(course)
        if res < min_val:
            min_val = res
        if res > max_val:
            max_val = res
        return
    
    
    for i in range(len(oper)):
        if not visited[i]:
            visited[i] = 1
            if oper[i] == "+":
                solution(idx + 1, res + nums[idx + 1], course + oper[i] + str(nums[idx + 1]))
            elif oper[i] == "-":
                solution(idx + 1, res - nums[idx + 1], course + oper[i] + str(nums[idx + 1]))
            elif oper[i] == "*":
                solution(idx + 1, res * nums[idx + 1], course + oper[i] + str(nums[idx + 1]))
            else:
                if (res < 0) or (nums[idx + 1] < 0):
                    solution(idx + 1, -1 * (abs(res) // abs(nums[idx + 1])), course + oper[i] + str(nums[idx + 1]))
                else:
                    solution(idx + 1, res // nums[idx + 1], course + oper[i] + str(nums[idx + 1]))
            visited[i] = 0


num_cnt = int(input())
nums = list(map(int, input().split()))
plus_cnt, minus_cnt, multi_cnt, divid_cnt = map(int, input().split())
oper = (['+'] * plus_cnt) + (['-'] * minus_cnt) + (['*'] * multi_cnt) + (['/'] * divid_cnt)
visited = [0] * len(oper)
max_val = -(1000000001)
min_val = 1000000001
solution(0, nums[0], '')
print(max_val)
print(min_val)