n = int(input())
body_list = []
score_list = []

for i in range(n):
    body_list.append(list(map(int, input().split())))

for i in body_list:
    body = 0
    for j in body_list:
        if i[0] < j[0] and i[1] < j[1]:
            body += 1
    score_list.append(body+1)

for i in score_list:
    print(i, end=' ')
