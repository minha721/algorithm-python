train = []
for i in range(4):
    train.append(list(map(int, input().split())))

res = [0]

for i in range(4):
    res.append(res[i]-train[i][0]+train[i][1])

print(max(res))