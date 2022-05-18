bit = input()

for i in range(len(bit)):
    if bit[i] == '1':
        one = i
        break
cutBit = bit[one:]

cnt = 0
target = cutBit[0]

for i in range(1, len(cutBit)):
    if cutBit[i] != target:
        cnt += 1
        target = cutBit[i]

print(cnt + 1)