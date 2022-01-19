from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))

pick_list = combinations(card, 3)
sum_list = []

for i in pick_list:
    sum = 0
    for j in i:
        sum += j

    if sum <= m:
        sum_list.append(sum)

print(max(sum_list))
