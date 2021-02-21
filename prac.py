N = int(input())
total_voted = int(input())
voted = list(map(int, input().split()))

candidates = {}
for i in range(total_voted):
    if candidates.get(voted[i]):
        candidates[voted[i]] += 1
    else:
        # 이미 사진올리는 틀이 꽉찼을 때
        if len(candidates) == N:
            min = total_voted
            # 작은 값을 구한다.
            for idx in candidates:
                if candidates[idx] < min:
                    min = candidates[idx]
                    remove = idx
            # 딕셔너리에서도 삭제
            del (candidates[remove])

        # 사진 틀에 추가
        candidates[voted[i]] = 1
    
    # 오래된 순서를 값으로 처리    
    for n in candidates:
        candidates[n] -= 0.00001
        
# ans = sorted(candidates)
# print(*ans)