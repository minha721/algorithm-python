from itertools import combinations

num = list(map(int, input().split()))
sum_list = []

for i in combinations(num, 3):
    sum_list.append(sum(i))

sum_sort = sorted(list(set(sum_list)), reverse=True)

print(sum_sort[4])