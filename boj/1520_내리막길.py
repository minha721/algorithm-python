def dfs(sy, sx):
    # 목적지 도착시 목적지까지 도착한 한 가지 경우가 되므로 1리턴
    if sy == M - 1 and sx == N - 1:
        return 1

    # 방문하지 않은 곳이라면 탐색
    if dp[sy][sx] == -1:
        # 이동했으니 마킹
        dp[sy][sx] = 0

        for i in range(4):
            ny = sy + dy[i]
            nx = sx + dx[i]

            if 0 <= ny < M and 0 <= nx < N:
                if graph[ny][nx] < graph[sy][sx]:
                    # 4방향 탐색해서 조건 만족하면 이전에 구한 값 더해서 dp 리스트 업데이트
                    dp[sy][sx] += dfs(ny, nx)

    # 방문했던 곳이라면 탐색 진행하지 않고 값을 업데이트(0인 경우 목적지까지 도달 불가, n인 경우 목적지까지 가는 경우의 수가 n개)
    return dp[sy][sx]

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

print(dfs(0, 0))

# print(dp)
# 문제 예제 입력시 [[3, 2, 2, 2, 1], [1, -1, -1, 1, 1], [1, -1, -1, 1, -1], [1, 1, 1, 1, -1]] 출력