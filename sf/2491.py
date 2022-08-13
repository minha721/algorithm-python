N = int(input())
num = list(map(int, input().split()))
dpDown, dpUp = [1]*N, [1]*N

for i in range(1, N):
    if num[i-1] >= num[i]:
        dpDown[i] = max(dpDown[i], dpDown[i-1]+1)
    if num[i-1] <= num[i]:
        dpUp[i] = max(dpUp[i], dpUp[i-1]+1)

print(max(max(dpDown), max(dpUp)))