word1, word2 = input().split()
res = [['.'] * len(word1) for _ in range(len(word2))]
word1_idx = -1
word2_idx = -1

for i in range(len(word1)):
    for j in range(len(word2)):
        if word1[i] == word2[j]:
            word1_idx = i
            word2_idx = j
            break
        
    if word1_idx >= 0:
        break

for i in range(len(word2)):
    if i == word2_idx:
        for k in range(len(word1)):
            res[i][k] = word1[k]

    for j in range(len(word1)):
        if j == word1_idx:
            res[i][j] = word2[i]

for i in range(len(res)):
    print(''.join(res[i]))
