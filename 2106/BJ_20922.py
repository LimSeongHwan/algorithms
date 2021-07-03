nums_length, same_cnt = map(int, input().split())
nums = list(map(int, input().split()))
num_cnt = [0] * 100001
max_num_length = 0
start = 0
end = 1
num_length = 1
num_cnt[nums[start]] += 1

while end < nums_length:
    num_cnt[nums[end]] += 1
    num_length += 1

    if num_cnt[nums[end]] > same_cnt:
        max_num_length = max(num_length - 1, max_num_length)

        while num_cnt[nums[end]] > same_cnt:
            num_cnt[nums[start]] -= 1
            num_length -= 1
            start += 1

    end += 1

print(max(max_num_length, num_length))