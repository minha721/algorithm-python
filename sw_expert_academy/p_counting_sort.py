array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
res = []

cnt = [0] * (max(array) + 1)

for i in array:
    cnt[i] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

# 각 숫자 별로 갯수가 1 이상이면 그 갯수만큼 해당 숫자 res에 append
for i in range(len(cnt)):
    if cnt[i] != 0:
        for j in range(cnt[i]):
            res.append(i)

print(res)
