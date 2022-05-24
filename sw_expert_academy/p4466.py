N, K = map(int, input().split())
score = list(map(int, input().split()))
score.sort(reverse=True)

sum = 0
for i in range(K):
    sum += score[i]

print(sum)