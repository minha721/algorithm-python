N = int(input())
num_six = '666'
num = 666
cnt = 0

while True:
    if num_six in str(num):
        cnt += 1
    if cnt == N:
        break
    num += 1

print(num)