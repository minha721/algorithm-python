# 백트래킹 풀이
def dfs(idx, total):
    global answer

    if idx == N:
        if total >= B:
            answer = min(answer, total - B)
        return

    dfs(idx + 1, total + height[idx])
    dfs(idx + 1, total)

T = int(input())

for tc in range(T):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    answer = 1e9
    dfs(0, 0)

    print("#{} {}".format(tc + 1, answer))

# 부분 집합 풀이 -> 똑같은거 같은데?
# def subset(cnt):
#     global answer
#
#     if cnt == N:
#         height_sum = 0
#         for i in range(N):
#             if isSelected[i]:
#                 height_sum += height[i]
#
#         if height_sum >= B:
#             answer = min(answer, height_sum - B)
#         return
#
#     isSelected[cnt] = True
#     subset(cnt + 1)
#     isSelected[cnt] = False
#     subset(cnt + 1)
#
# T = int(input())
#
# for tc in range(T):
#     N, B = map(int, input().split())
#     height = list(map(int, input().split()))
#     isSelected = [False for _ in range(N)]
#
#     answer = 1e9
#     subset(0)
#
#     print("#{} {}".format(tc + 1, answer))
