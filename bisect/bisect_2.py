N, M = map(int, input().split())
tree = list(map(int, input().split()))

start = 1
end = max(tree)

while start <= end:
    sum = 0
    mid = (start + end) // 2
    for i in tree:
        if i >= mid :
            sum += (i - mid)

    if sum >= M:
        start = mid + 1
    else:
        end = mid -1

print(end)