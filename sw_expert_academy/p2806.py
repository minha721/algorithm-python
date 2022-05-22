N = int(input())
graph = [0] * N
res = 0


def is_possible(x):
    # 위에서부터 퀸을 놓으므로 현재 행보다 이전의 행들만 확인하면 됨
    for i in range(x):
        # 같은 열이나 대각선에 퀸이 있다면 False 리턴
        if graph[x] == graph[i] or abs(graph[x] - graph[i]) == abs(x - i):
            return False
    return True


def n_queens(x):
    global res

    # 모든 행을 다 탐색했으면 res 1 증가
    if x == N:
        res += 1
    else:
        # x행에서 반복문 돌면서 i열에 놓는 것이 가능한지 확인
        for i in range(N):
            graph[x] = i
            # 가능하다면 다음 행 확인
            # 가능하지 않다면 다음 열 확인
            if is_possible(x):
                n_queens(x + 1)


n_queens(0)
print(res)