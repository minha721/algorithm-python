N = int(input())
score = list(map(float, input().split()))
result = 0
max = max(score)

for i in range(N):
    result += (score[i]/max*100)

print(result/N)