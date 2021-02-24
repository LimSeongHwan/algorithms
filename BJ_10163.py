paper_num = int(input())
area = [[0] * 101 for _ in range(101)] 
sum_list = [0] * (paper_num + 1)
papers = []

for _ in range(paper_num):
    papers.append(list(map(int, input().split())))

for i in range(paper_num):
    for j in range(papers[i][3]):
        for k in range(papers[i][2]):
            area[papers[i][1]+j][papers[i][0]+k] = i+1
            
for i in range(len(area)):
    for j in range(len(area[0])):
        if area[i][j]:
            sum_list[area[i][j]] += (area[i][j] // area[i][j])

print('\n'.join(map(str, sum_list[1:])))
