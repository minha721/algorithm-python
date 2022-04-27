import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    
    if highland[x][y] == 0:
        return False

    highland[x][y] = 0
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)

    return True

T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())
    highland = [[0]*M for _ in range(N)]
    for j in range(K):
        X, Y = map(int, input().split())
        highland[Y][X] = 1

    result = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j) == True:
                result += 1
    print(result)