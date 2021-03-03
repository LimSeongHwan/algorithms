def solution(case):
    divisors = list(map(int, input().split()))
    divisors.sort()
    return divisors[0] * divisors[-1]


case = int(input())
print(solution(case))