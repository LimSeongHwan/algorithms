N, K = map(int, input().split())
medal_list = []

for _ in range(N):
    medal_list.append(list(map(int, input().split())))

# 버블정렬 식으로 진행
for n in range(len(medal_list)):
    for i in range(len(medal_list)-1):
        if medal_list[i][1] < medal_list[i+1][1]:       # 금메달이 높은 경우 위치 변경
            medal_list[i], medal_list[i+1] = medal_list[i+1], medal_list[i]

        elif medal_list[i][1] == medal_list[i+1][1] and medal_list[i][2] < medal_list[i+1][2]:  # 금메달이 같고, 은메달이 높은 경우 위치 변경
            medal_list[i], medal_list[i + 1] = medal_list[i + 1], medal_list[i]

        elif medal_list[i][1] == medal_list[i+1][1] and medal_list[i][2] == medal_list[i+1][2] and medal_list[i][3] < medal_list[i+1][3]:
            medal_list[i], medal_list[i + 1] = medal_list[i + 1], medal_list[i] # 금, 은메달이 같고 동메달이 높은 경우 위치 변경


for i in range(len(medal_list) - 1):    # 모든 메달이 같은 상황일 때, 한 인덱스로 모으고 그 뒤 인덱스에 [0, 0, 0, 0] 추가
    if (medal_list[i][1] == medal_list[i+1][1]) and (medal_list[i][2] == medal_list[i+1][2]) and (medal_list[i][3] == medal_list[i+1][3]):
        medal_list[i] = [medal_list[i],medal_list[i+1]]
        medal_list[i+1] = [0, 0, 0, 0]
        
# 정렬 완료된 상황

for i in range(len(medal_list)):
    if type(medal_list[i][0]) == int:   # 동순위 상황이 아닌 일반적인 등수일 때
        if medal_list[i][0] == K:       # 0번 인덱스가 찾던 국가 값과 같으면 +1 하여 출력
            print(i+1)
    else:                               # 동순위 상황이라 타입이 list 일 때
        for medals in (medal_list[i]):  # 리스트 안 리스트를 둘러보면서 0번 인덱스가 찾던 국가 값과 같으면
            if medals[0] == K:          # +1하여 출력
                print(i+1)