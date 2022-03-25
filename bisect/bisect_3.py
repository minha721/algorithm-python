S = int(input())

if S == 1:
    print(1)
else:
    start = 1
    end = S

    while start <= end:
        mid = (start + end) // 2
        sum = (mid)*(mid + 1) / 2

        if sum > S:
            end = mid -1
        else:
            start = mid + 1

    print(end)