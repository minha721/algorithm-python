N, X = map(int, input().split())

pos = 0
num = 0
for i in reversed(str(X)):
    num += int(i) * pow(N, pos)
    pos += 1

print(num % (N - 1))