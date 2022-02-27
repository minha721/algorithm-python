num = list(map(int, input().split()))
squareSum = 0

for i in range(len(num)):
    squareSum += num[i] ** 2

print(squareSum%10)