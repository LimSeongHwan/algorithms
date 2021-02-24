'''
BOJ1713 - 후보 추천하기 (구현, 시뮬레이션)
'''
N = int(input())
total_vote = int(input())
vote_list = list(map(int, input().split())) # input 셋째줄 추천 목록
vote_count = [0] * 101  # 인덱스별 추천 집계 현황
vote_aging = [0] * 101  # 인덱스별 언제 갱신 되었는 지 기록
answer = []

for i in range(total_vote): # 투표별 반복
    min_vote = 987654321  # 최저 추천 횟수 (방출 대상)
    min_aging = 987654321 # 가장 갱신이 오래된 인덱스 (동일 추천 조건 우선 방출 대상)

    for vote_c in vote_count:
        if vote_c >= 1:             # 전체 집계 현황에서 1 이상이면서 min보다 작은 값을 최소 추천으로 갱신
            if vote_c < min_vote:
                min_vote = vote_c

    if vote_count[vote_list[i]] > 0:    # i번째 추천이 기존 집계에 있을 경우 추천수만 증가
        vote_count[vote_list[i]] += 1
        vote_aging[vote_list[i]] = i    # i번째 인덱스 때 갱신했음을 기록 (값이 작을수록 오래된 것)



    elif N >= 1:    # 남아있는 사진틀이 1개 이상일 때 / elif vote_count[vote_list[i]] == 0 and N >= 1도 틀림
        vote_count[vote_list[i]] += 1   # 사진틀을 1개 줄이고 i에 해당하는 카운트와 갱신 기록
        vote_aging[vote_list[i]] = i
        N -= 1

    elif N < 1: # 더 이상 남은 사진틀이 없을 때 / elif vote_count[vote_list[i]] == 0 and N < 1도 틀림
        for j in range(101):                                            # 전체 추천집계와 갱신 시간을 검토
            if vote_count[j] == min_vote and vote_aging[j] < min_aging: # 추천수가 최소일 때의 최소 인덱스 갱신 (방출대상 j)
                min_aging = vote_aging[j]
        for j in range(101):
            if vote_count[j] == min_vote and vote_aging[j] == min_aging: # 방출 대상 j의 추천수를 0으로 초기화
                vote_count[j] = 0                                        # 에이징을 역으로 높은값 987654321로 줘도 틀림
                vote_aging[j] = 0

        vote_count[vote_list[i]] += 1   # 방출 이후 기존 대상 i의 카운트와 갱신 기록
        vote_aging[vote_list[i]] = i
        print("vote_count = ", vote_count)
        print("vote_aging = ",vote_aging)
        print()
for i in range(len(vote_count)):    # 전체 집계 중 0 이상의 추천 후보자만 오름차순으로 answer 리스트에 추가
    if vote_count[i] > 0:
        answer.append(i)

for ans in answer:
    print(ans, end=" ") # 정답인 각 후보 한칸 씩 띄워가며 출력