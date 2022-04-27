map = [list(map(str, input().split())) for _ in range(5)]
nums = []

def dfs(x, y, number):
    if len(number) == 6:
        if number not in nums:
            nums.append(number)
        return

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx <= 4 and 0 <= ny <= 4:
            dfs(nx, ny, number+map[nx][ny])

for i in range(5):
    for j in range(5):
        dfs(i, j, map[i][j])

print(len(nums))