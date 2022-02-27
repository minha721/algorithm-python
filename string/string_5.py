T = int(input())

for i in range(T):
    result = ''
    R, string = map(str, input().split())

    for i in range(len(string)):
        char = string[i]
        result += char * int(R)

    print(result)