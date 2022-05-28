def A(liter, cost):
    return cost * liter


def B(liter, target, basic, cost):
    if liter <= target:
        return basic
    else:
        return basic + (cost * (liter - target))


T = int(input())

for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    print("#{} {}".format(test_case, min(A(W, P), B(W, R, Q, S))))