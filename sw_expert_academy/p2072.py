T = int(input())

for t in range(1, T + 1):
    nums = list(map(int, input().split()))
    sum = 0

    for num in nums:
        if num % 2 == 1:
            sum += num

    print("#{} {}".format(t, sum))