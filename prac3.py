def solution(N):

    def solution2(idx, start, arr):
        if sum(arr) > N:
            return
        if sum(arr) == N:
            res.append(arr)
            return
        else:
            for i in range(start, len(nums)):
                solution2(idx + 1, i + 1, arr + [nums[i]])


    nums = [i for i in range(1, N + 1)]
    max_length = 0
    res = []
    ans = []
    solution2(0, 0, [])

    for nums in res:
        flag = True
        for num in nums:
            if (not num % 2):
                flag = False
                break
        if flag:
            if len(nums) > max_length:
                ans = nums
                max_length = len(nums)

    return ans