def solution(case):

    def factorial(number):
        if number == 0:
            return 1
        elif number == 1:
            return number

        return number * factorial(number - 1)

    n, m = map(int, input().split())
    res = factorial(m) / (factorial(n) * factorial(m - n))
    return int(res)

case = int(input())
for _ in range(case):
    print(solution(case))
        