picture_frame = int(input())
picture_number = int(input())
pictures = []
recommend_cnt = dict()
recommend_person = list(map(int, input().split()))

for person_num in recommend_person:
    if person_num in recommend_cnt:
        recommend_cnt[person_num] += 1
    else:
        if len(pictures) == picture_frame:
            min_values = []
            for key, value in recommend_cnt.items():
                if min(recommend_cnt.values()) == value:
                    min_values.append(key)
            for person in pictures:
                if person in min_values:
                    pictures.remove(person)
                    del recommend_cnt[person]
                    break

        pictures.append(person_num)
        recommend_cnt[person_num] = 1

pictures.sort()
print(' '.join(map(str, pictures)))