word = input()
split= []

for i in range(1, len(word)-1):
    for j in range(i + 1, len(word)):
        first = "".join(reversed(word[:i]))
        second = "".join(reversed(word[i:j]))
        third = "".join(reversed(word[j:]))
        split.append(first+second+third)

split.sort()
print(split[0])