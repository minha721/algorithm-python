string = input()
res = []

for i in range(97, 123):
    char = chr(i)
    res.append(str(string.find(char)))

print(" ".join(res))