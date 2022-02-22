str = input()
length = len(str)
flag = 1

for i in range(length//2):
    if str[i] != str[length - i - 1]:
        flag = 0
        break

print(flag)