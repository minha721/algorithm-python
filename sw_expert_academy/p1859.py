T = int(input())

for i in range(T):
    price = []

    N = int(input())
    price = list(map(int, input().split()))

    answer = 0
    max = price[-1]
    for j in range(N-2, -1, -1):
        if price[j] < max:
            answer += (max - price[j])
        else:
            max = price[j]

    print("#{} {}".format(i + 1, answer))